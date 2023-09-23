# Tyler Tobin
# Learning Python Unit Test Module
# Unit Tests

import unittest
import functions_unit

class TestFunction(unittest.TestCase):

    def testAdd(self):
        
        result = functions_unit.add(4, 6)
        resultNeg = functions_unit.add(-4, 6)
        
        self.assertEqual(result, 10)
        self.assertEqual(resultNeg, 2)

    def testSub(self):
        
        result = functions_unit.subtract(10, 6)
        resultNeg = functions_unit.subtract(-10, 6)
        
        self.assertEqual(result, 4)
        self.assertEqual(resultNeg, -16)

    def testMultiply(self):
        
        result = functions_unit.multiply(5, 4)
        resultNeg = functions_unit.multiply(-2, 5)
        
        self.assertEqual(result, 20)
        self.assertEqual(resultNeg, -10)

    def testDivide(self):
        
        result = functions_unit.divide(12, 3)
        resultNeg = functions_unit.divide(-12, 4)

        # Planned Error
        
        self.assertEqual(result, 4)
        self.assertEqual(resultNeg, -5)

    

if __name__ == '__main__':
    unittest.main()
