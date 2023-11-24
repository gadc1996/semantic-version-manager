from setuptools import setup, find_packages
from semversion import Version

setup(
    name="semversion",
    version=Version.get(),
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "semversion=semversion.__main__:main",
        ],
    },
)
