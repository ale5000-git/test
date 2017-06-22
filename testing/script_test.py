import unittest
from script import func1

class ScriptTestCase(unittest.TestCase):
    """Tests for `script.py`."""

    def test_func1_return(self):
        """...?"""
        self.assertTrue(func1())

if __name__ == '__main__':
    unittest.main()
