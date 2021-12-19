import unittest
from Calc import Calc
#Test cases to test Calulator methods
#You always create  a child class derived from unittest.TestCase
class test(unittest.TestCase):
  #setUp method is overridden from the parent class TestCase
  def setUp(self):
    self.Calc = Calc()
  #Each test method starts with the keyword test_
  def test_add(self):
    self.assertEqual(self.Calc.Calculator.arithmetic_operation.add(4,7), 11)
  def test_subtract(self):
    self.assertEqual(self.Calc.Calculator.arithmetic_operation.sub(10,5), 5)
  def test_multiply(self):
    self.assertEqual(self.Calc.Calculator.arithmetic_operation.multi(3,7), 21)
  def test_divide(self):
    self.assertEqual(self.Calc.Calculator.arithmetic_operation.divi(10,2), 5)
  def test_modulus(self):
    self.assertEqual(self.Calc.Calculator.more.mod(3,2), 1)
  def test_exponential(self):
    self.assertEqual(self.Calc.Calculator.more.expo(2,3), 8)
  def test_floor(self):
    self.assertEqual(self.Calc.Calculator.more.floor(3,1), 1)
# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()