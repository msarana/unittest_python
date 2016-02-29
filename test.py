'''
Created on Feb 27, 2016

@author: Maria
'''
import unittest


class Test(unittest.TestCase):


    def testName(self):
        pass
    
    def testName2(self):
        self.assertEqual('a', 'A')
        


    
if __name__ == '__main__': 
    import xmlrunner 
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
