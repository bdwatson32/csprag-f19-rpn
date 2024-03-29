import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +i')
        self.assertEqual(2, result)

    def test_sub(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
    def test_pow(self):
        result = rpn.calculate('2 4 ^')
        self.assertEqual(16, result)
    def test_badinput(self):
        with self.assertRaises(TypeError):


