#include <atlstr.h> // CW2A
#include <PhysicalMonitorEnumerationAPI.h>
#include <LowLevelMonitorConfigurationAPI.h>

#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <functional>
#include <sstream>

std::vector<PHYSICAL_MONITOR> physicalMonitors{};

BOOL CALLBACK monitorEnumProcCallback(HMONITOR hMonitor, HDC hDeviceContext, LPRECT rect, LPARAM data)
{
	DWORD numberOfPhysicalMonitors;
	BOOL success = GetNumberOfPhysicalMonitorsFromHMONITOR(hMonitor, &numberOfPhysicalMonitors);
	if (success) {
		auto originalSize = physicalMonitors.size();
		physicalMonitors.resize(physicalMonitors.size() + numberOfPhysicalMonitors);
		success = GetPhysicalMonitorsFromHMONITOR(hMonitor, numberOfPhysicalMonitors, physicalMonitors.data() + originalSize);
	}
	return true;
}

std::string toUtf8(wchar_t *buffer)
{
	CW2A utf8(buffer, CP_UTF8);
	const char* data = utf8.m_psz;
	return std::string{ data };
}

int printUsage(std::vector<std::string> args)
{
	std::cout << "Usage: winddcutil command [<arg> ...]" << std::endl
		<< "Commands:" << std::endl
		<< "\thelp                                           Display help" << std::endl 
		<< "\tdetect                                         Detect monitors" << std::endl
		<< "\tcapabilities <display-id>                      Query monitor capabilities" << std::endl
		<< "\tgetvcp <display-id> <feature-code>             Report VCP feature value" << std::endl
		<< "\tsetvcp <display-id> <feature-code> <new-value> Set VCP feature value" << std::endl;
	return 1;
}

int detect(std::vector<std::string> args)
{
	int i = 0;
	for (auto &physicalMonitor : physicalMonitors) {
		std::cout << "Display " << i << ":\t" << toUtf8(physicalMonitor.szPhysicalMonitorDescription) << std::endl;
		i++;
	}
	return 0;
}

int capabilities(std::vector<std::string> args) {
	if (args.size() < 1) {
		std::cerr << "Display ID required" << std::endl;
		return printUsage(args);
	}

	size_t displayId = INT_MAX;
	try {
		displayId = std::stoi(args[0]);
	}
	catch (...) {
		std::cerr << "Failed to parse display ID" << std::endl;
		return 1;
	}

	if (displayId > physicalMonitors.size() - 1) {
		std::cerr << "Invalid display ID" << std::endl;
		return 1;
	}

	auto physicalMonitorHandle = physicalMonitors[displayId].hPhysicalMonitor;

	DWORD capabilitiesStringLengthInCharacters;
	auto success = GetCapabilitiesStringLength(physicalMonitorHandle, &capabilitiesStringLengthInCharacters);
	if (!success) {
		std::cerr << "Failed to get capabilities string length" << std::endl;
		return 1;
	}

	std::unique_ptr<char[]> capabilitiesString{ new char[capabilitiesStringLengthInCharacters] };
	success = CapabilitiesRequestAndCapabilitiesReply(physicalMonitorHandle, capabilitiesString.get(), capabilitiesStringLengthInCharacters);
	if (!success) {
		std::cerr << "Failed to get capabilities string" << std::endl;
		return 1;
	}

	std::cout << std::string(capabilitiesString.get()) << std::endl;

	return 0;
}

int getVcp(std::vector<std::string> args) {
	if (args.size() < 1) {
		std::cerr << "Display ID required" << std::endl;
		return printUsage(args);
	}

	size_t displayId = INT_MAX;
	BYTE vcpCode;
	try {
		displayId = std::stoi(args[0]);
		vcpCode = std::stoul(args[1], nullptr, 16);
	}
	catch (...) {
		std::cerr << "Failed to parse display ID" << std::endl;
		return 1;
	}

	if (displayId > physicalMonitors.size() - 1) {
		std::cerr << "Invalid display ID" << std::endl;
		return 1;
	}

	auto physicalMonitorHandle = physicalMonitors[displayId].hPhysicalMonitor;

	DWORD currentValue;
	bool success = GetVCPFeatureAndVCPFeatureReply(physicalMonitorHandle, vcpCode, NULL, &currentValue, NULL);
	if (!success) {
		std::cerr << "Failed to get the vcp code value" << std::endl;
		return 1;
	}

	std::stringstream ss;
	ss << std::hex << currentValue;
	std::cout << "VCP " << args[1] << " " << ss.str() << std::endl;

	return 0;
}

int setVcp(std::vector<std::string> args) {
	if (args.size() < 3) {
		std::cerr << "Invalid number of arguments" << std::endl;
		return printUsage(args);
	}

	size_t displayId = INT_MAX;
	BYTE vcpCode;
	DWORD newValue;
	try {
		displayId = std::stoi(args[0]);
		vcpCode = std::stoul(args[1], nullptr, 16);
		newValue = std::stoul(args[2], nullptr, 16);
	}
	catch (...) {
		std::cerr << "Failed to parse setvcp arguments" << std::endl;
		return printUsage(args);
	}

	if (displayId > physicalMonitors.size() - 1) {
		std::cerr << "Invalid display ID" << std::endl;
		return 1;
	}

	bool success = SetVCPFeature(physicalMonitors[displayId].hPhysicalMonitor, vcpCode, newValue);
	if (!success) {
		std::cerr << "Failed to set vcp feature" << std::endl;
		return 1;
	}
	return 0;
}

std::unordered_map<std::string, std::function<int(std::vector<std::string>)>> commands
{
	{ "help", printUsage },
	{ "detect", detect},
	{ "capabilities", capabilities },
	{ "getvcp", getVcp },
	{ "setvcp", setVcp},
};


int main(int argc, char *argv[], char *envp[])
{
	std::vector<std::string> args;

	if (argc < 2)
		return printUsage(args);

	for (int i = 1; i < argc; i++) {
		std::string arg(argv[i]);
		args.emplace_back(arg);
	}

	auto command = commands.find(args[0]);
	if (command == commands.end()) {
		std::cerr << "Unkown command" << std::endl;
		return printUsage(args);
	}
	args.erase(args.begin());

	EnumDisplayMonitors(NULL, NULL, &monitorEnumProcCallback, 0);

	auto success = command->second(args);

	DestroyPhysicalMonitors(physicalMonitors.size(), physicalMonitors.data());

	return success;
}
