#!/usr/bin/env python3
from setuptools import setup
setup(
    name="tap-greenhouse",
    version="0.1.1",
    description="Singer.io tap for extracting data",
    author="Simon Data",
    url="http://simondata.com",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_greenhouse"],
    install_requires=[
        "singer-python==5.9.0",
        'requests==2.18.4',
        "pendulum==1.2.0",
        "tap-kit @ git+https://github.com/killianbrackey/tap-kit@master"
    ],
    dependency_links=[
        "https://github.com/Radico/tap-kit/tarball/master#egg=tap-kit-0.1.1",
    ],
    entry_points="""
    [console_scripts]
    tap-greenhouse=tap_greenhouse:main
    """,
    packages=["tap_greenhouse", "tap_greenhouse.streams"],
    include_package_data=True,
)
