import unittest
from mathfunc import *


class TestMathFunc01(unittest.TestCase):
    m_ignore = True
    """Test mathfuc.py"""
    @classmethod
    def setUpClass(cls):
        print "do something before test.Prepare environment."

    @classmethod
    def tearDownClass(cls):
        print "do something after test.Clean up."

    @unittest.skipIf(m_ignore, "i do not want to run this test")
    def test_add(self):
        """Test method add(a, b)"""
        print('test_add')
        
        self.assertEqual(120, add(100, 20))
        self.assertNotEqual(3, add(10, 10))

    def test_minus(self):
        """Test method minus(a, b)"""
        print('test_minus');
        self.assertEqual(90, minus(100, 10))


if __name__ == '__main__':
    unittest.main()