#!/usr/bin/env python

import setuptools

def custom_test_suite():
    import unittest
    return unittest.TestLoader().discover("tests", pattern="*_test.py")

setuptools.setup(
    name="Test-1",
    test_suite="setup.custom_test_suite"
)
