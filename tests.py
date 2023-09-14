import pytest
from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calculator = Calculator
    def test_adding(self):
        assert self.calculator.adding(self, 1, 1) == 2
    def test_substraction(self):
        assert self.calculator.substraction(self, 2, 1) == 1
    def test_multiply(self):
        assert self.calculator.multiply(self, 2, 2) == 4
    def test_division(self):
        assert self.calculator.division(self, 4, 2) == 2