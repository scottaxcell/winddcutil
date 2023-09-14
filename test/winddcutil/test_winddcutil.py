import subprocess
import time
from pathlib import Path

WINDDCUTIL_EXE = (
    Path(__file__).parent.parent.parent.absolute() / "dist" / "winddcutil.exe"
)

"""
NOTICE

Do not expect the following tests to work for you!

The tests have been written against a specific hardware configuration, a VG27AQ monitor with the HDMI-2 input source selected.
"""


def test_detect() -> None:
    """Checks the detect value has 2 generic monitors connected."""
    process = subprocess.run(
        [WINDDCUTIL_EXE, "detect"], capture_output=True, text=True, check=True
    )
    expected = "1 Generic PnP Monitor|2 Generic PnP Monitor"
    result = "|".join(process.stdout.splitlines())
    assert result == expected


def test_capabilities() -> None:
    """Checks the capabilities value."""
    process = subprocess.run(
        [WINDDCUTIL_EXE, "capabilities", "1"],
        capture_output=True,
        text=True,
        check=True,
    )
    expected = "(prot(monitor)type(lcd)model(VG27AQ)cmds(01 02 03 07 0C 4E F3 E3)vcp(02 04 05 08 10 12 14(05 06 08 0B) 16 18 1A 52 60( 11 12 0F) 62 87 8A 8D(01 02) AC AE B6 C0 C6 C8 C9 CC( 01 02 03 04 05 06 07 08 09 0A 0C 0D 11 12 14 1A 1E 1F 30 23 31) D6(01 04 05) DF E2(00 01 02 03 04 05) E4(00 01) E6(00 01) E7(00 01) E9(00 01) EA(00 01) EB(00 01) EF(00 01 02 03) F0(00 01 02 03 04) ) mswhql(1)mccs_ver(2.2)asset_eep(32)mpu_ver(01))"
    result = "|".join(process.stdout.splitlines())
    assert result == expected


def test_getvcp() -> None:
    """Checks the selected input source is HDMI-2."""
    process = subprocess.run(
        [WINDDCUTIL_EXE, "getvcp", "1", "0x60"],
        capture_output=True,
        text=True,
        check=True,
    )
    expected = "VCP 0x60 15"
    result = "|".join(process.stdout.splitlines())
    assert result == expected


def test_setvcp() -> None:
    """Checks the contrast is set to 10. The contrast is then set to the OG value."""
    process = subprocess.run(
        [WINDDCUTIL_EXE, "getvcp", "1", "0x12"],
        capture_output=True,
        text=True,
        check=True,
    )
    og_contrast = process.stdout.splitlines()[-1].split(" ")[-1]

    process = subprocess.run(
        [WINDDCUTIL_EXE, "setvcp", "1", "0x12", "10"],
        capture_output=True,
        text=True,
        check=True,
    )

    time.sleep(2)

    process = subprocess.run(
        [WINDDCUTIL_EXE, "getvcp", "1", "0x12"],
        capture_output=True,
        text=True,
        check=True,
    )
    expected = "VCP 0x12 10"
    contrast = process.stdout.splitlines()[-1]
    assert contrast == expected

    process = subprocess.run(
        [WINDDCUTIL_EXE, "setvcp", "1", "0x12", og_contrast],
        capture_output=True,
        text=True,
        check=True,
    )
