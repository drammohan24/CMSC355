import exponent
import unittest

class TestPowerOf(unittest.TestCase):
	def test_integer(self):
		self.assertEqual(exponent.powerOf(5,2), 25)

if __name__ == '__main__':
	unittest.main()
