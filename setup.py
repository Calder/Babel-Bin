from setuptools import setup

setup(
    name="babel",
    version="0.1.0",
    author="Calder Coalson",
    author_email="caldercoalson@gmail.com",
    packages=["babel"],
    url="https://github.com/Calder/Babel-Bin",
    license="LICENSE.txt",
    description = "Useful towel-related stuff.",
    long_description=open("README.md").read(),
    install_requires=[
        "requests-futures",
        "twilio",
    ],
    entry_points={
        "console_scripts": [
            "babel=babel:main",
        ],
    },
)