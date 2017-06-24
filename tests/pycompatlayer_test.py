import unittest
import pycompatlayer


class PyCompatLayerTestCase(unittest.TestCase):
    """Tests for `pycompatlayer.py`."""

    def test_fix_all(self):
        self.assertTrue(pycompatlayer.fix_all())

if __name__ == '__main__':
    unittest.main()
