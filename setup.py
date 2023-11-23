from setuptools import setup, find_packages
from semantic_versioning import Version

setup(
    name='semantic-versioning',
    version= Version.get(),
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'semantic-versioning=semantic_versioning.__main__:main',
        ],
    },
)
