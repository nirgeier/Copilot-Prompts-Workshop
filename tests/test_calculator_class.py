import pytest
from calculator.calculator import Calculator

class TestCalculator:
    def test_add_list(self):
        calc = Calculator()
        assert calc.add([1.0, 2.0, 3.0]) == 6.0
        assert calc.add([]) == 0.0
        assert calc.add([-1.0, 1.0]) == 0.0

    def test_subtract_list(self):
        calc = Calculator()
        # 10 - 2 - 3 = 5
        assert calc.subtract([10.0, 2.0, 3.0]) == 5.0
        # 10 - (-2) = 12
        assert calc.subtract([10.0, -2.0]) == 12.0
        assert calc.subtract([5.0]) == 5.0
        assert calc.subtract([]) == 0.0
