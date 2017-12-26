#coding=utf-8
import random  
import unittest  
      
class TestSequenceFunctions(unittest.TestCase):  
      
    def setUp(self):  
        self.seq = range(10)
        print('setUp called')
      
    def test_shuffle(self):  
        print('test_shuffle called')
        # make sure the shuffled sequence does not lose any elements  
        random.shuffle(self.seq)  
        self.seq.sort()  
        self.assertEqual(self.seq, range(10))  
      
        # should raise an exception for an immutable sequence  
        self.assertRaises(TypeError, random.shuffle, (1,2,3))  
      
    def test_choice(self):  
        print('test_choice')
        element = random.choice(self.seq)  
        self.assertTrue(element in self.seq)  
      
    def test_sample(self):  
        print('test_sample')
        with self.assertRaises(ValueError):  
            random.sample(self.seq, 20)  
        for element in random.sample(self.seq, 5):  
            self.assertTrue(element in self.seq)  
      
if __name__ == '__main__':  
        unittest.main()  