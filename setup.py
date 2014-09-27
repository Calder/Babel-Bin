from setuptools import *

setup(
    name="babel",
    version="0.3.0",
    author="Calder Coalson",
    author_email="caldercoalson@gmail.com",
    url="https://github.com/Calder/Babel-Bin",
    description = "Foo bar",
    long_description=open("README.txt").read(),
    license="LICENSE.txt",
    
    install_requires=[
        "requests-futures",
        "twilio",
    ],
    zip_safe=True,

    packages=["babel"],
    entry_points={
        "console_scripts": [
            "babel=babel:main",
        ],
    },
)

import sys
if sys.prefix != "/usr/local/bin":
    import subprocess
    subprocess.call(["ln", "-sf",
                     "%s/bin/babel" % sys.prefix, 
                     "/usr/local/bin/babel"])