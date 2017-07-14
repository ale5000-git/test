#!/usr/bin/env python

import unittest
import main

class MainTestCase(unittest.TestCase):
    def test_fix_all(self):
        self.assertTrue(main.fix_all())
