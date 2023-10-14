import unittest
import sys
sys.path.append(r'/Users/nikitatunaev/Desktop/laba_1/task1')
from task1 import plus, minus, multiply, divide

class CalculatorTestCase(unittest.TestCase):

    # Тест для проверки работы, можно удалить
    def test_plus(self):
        self.assertEqual(plus(2, 2), f"Result: {4}")
    
    def test_minus(self):
        self.assertEqual(minus(5, 2), f"Result: {3}")         
    
    def test_multiply(self):
        self.assertEqual(multiply(5, 2), f"Result: {10}")
    
    def test_divide(self):
        self.assertEqual(divide(10, 2), f"Result: {float(5)}")
