import exponent
import unittest

class TestPowerOf(unittest.TestCase):
        def test_integer(self):
                self.assertEqual(exponent.powerOf(3,0), 1)

if __name__ == '__main__':
        unittest.main()
