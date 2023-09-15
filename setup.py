from setuptools import setup

setup(
    name="winddcutil",
    version="0.1.0",
    packages=["winddcutil"],
    entry_points={"console_scripts": ["winddcutil = winddcutil.__main__:main"]},
    install_requires=[
        "monitorcontrol @ git+https://github.com/scottaxcell/monitorcontrol.git@0befac81d29331fb4d062e45af23d4804e54bb55"
    ],
)
