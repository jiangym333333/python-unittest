# -*- coding: utf-8 -*-

import unittest
from test_mathfunc import TestMathFunc
from test_mathFun01 import TestMathFunc01

if __name__ == '__main__':
    print('call test_suite...');
    suite = unittest.TestSuite()

    #tests = [TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    #suite.addTests(tests)

    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
    
    suite01= unittest.TestSuite()
    suite01.addTest(TestMathFunc01('test_minus'))
    suite.addTests(suite01)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)