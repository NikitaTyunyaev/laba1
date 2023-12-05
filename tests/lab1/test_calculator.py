import unittest
import sys
sys.path.append(r'/Users/nikitatunaev/Desktop/laba_1/src')
import calculator as calc 

class CalculatorTestCase(unittest.TestCase):

    # Тест для проверки работы, можно удалить
    def test_plus(self):
        self.assertEqual(calc.plus(2, 2), f"Result: {4}")
    
    def test_minus(self):
        self.assertEqual(calc.minus(5, 2), f"Result: {3}")         
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(5, 2), f"Result: {10}")
    
    def test_divide(self):
        self.assertEqual(calc.divide(10, 2), f"Result: {float(5)}")

if __name__ == "__main__":
    unittest.main()
