from distutils.core import setup
from setuptools import find_packages
from nwk import __version__


setup(
    name="Nightwrest Keep",
    version=__version__,
    packages=find_packages(),
    package_data={"nwk": ["assets/scenes/*.xml"]},
    url="https://github.com/mtaylor33/NightwrestKeep",
    license="MIT",
    author="Marcus T Taylor",
    description="Sample text-based adventure game set in the town of Nightwrest.",
    long_description=open("README.md", "r").read(),
    install_requires=["termcolor>=1.1", "xmltodict>=0.12"],
    python_requires=">=3.0",
    entry_points={"console_scripts": ["nwk=nwk.play:main"]},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Games/Entertainment :: Role-Playing",
    ],
)
