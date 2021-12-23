import unittest
from calculation import Calculation
#Test cases to test Calulation methods
#You always create  a child class derived from unittest.TestCase
class test(unittest.TestCase):
  #setUp method is overridden from the parent class TestCase
  def setUp(self):
    self.Calc = Calculation()
  #Each test method starts with the keyword test_
  def test_add(self):
    self.assertEqual(self.Calc.addition(4,7), 11)
  def test_subtract(self):
    self.assertEqual(self.Calc.subtraction(10,5), 5)
  def test_multiply(self):
    self.assertEqual(self.Calc.multiplication(3,7), 21)
  def test_divide(self):
    self.assertEqual(self.Calc.division(10,2), 5)
  def test_modulus(self):
    self.assertEqual(self.Calc.modulo(3,2), 1)
  def test_exponential(self):
    self.assertEqual(self.Calc.exponential(2,3), 8)
  def test_floor(self):
    self.assertEqual(self.Calc.floor_division(3,1), 3)
# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()
