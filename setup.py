from setuptools import setup, find_packages

setup(
    name='semversion',
    version= "1.0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'semversion=semversion.__main__:main',
        ],
    },
)
