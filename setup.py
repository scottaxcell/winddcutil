from setuptools import setup

setup(
    name="winddcutil",
    version="0.1.0",
    packages=["winddcutil"],
    entry_points={"console_scripts": ["winddcutil = winddcutil.__main__:main"]},
    install_requires=["monitorcontrol>=3.0.3"],
)
