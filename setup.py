#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup for PyCompatLayer (The compatibility layer for Python)."""

import setuptools

#if sys.version_info <= (3, 2):
    #requires.append("configparser")

test_requirements = [
    "unittest2"
]

def custom_test_suite():
    import sys

    try:
        if sys.version_info <= (3, 4):
            import unittest2 as unittest
        else:
            import unittest
    except ImportError:
        import unittest
    return unittest.TestLoader().discover("tests", pattern="*_test.py")


setuptools.setup(
    zip_safe=True,
    name="PyCompatLayer",
    version="0.0.10-2",
    description="Compatibility layer for Python",
    long_description="See https://pypi.python.org/pypi/PyCompatLayer",
    url="https://github.com/ale5000-git/pycompatlayer",
    author="ale5000",
    author_email="nospam@nospam",
    license="LGPLv3+",
    platforms=["any"],
    py_modules=["pycompatlayer"],
    tests_require=test_requirements,
    test_suite="setup.custom_test_suite",

    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries :: Python Modules",

        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",

        ("License :: OSI Approved :: "
         "GNU Lesser General Public License v3 or later (LGPLv3+)"),
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ],

    # bugtrack_url="https://github.com/ale5000-git/pycompatlayer/issues",
    keywords="python python-library pycompatlayer compatlayer compatibility"
)
