import pytest
from calculator.calculator import Calculator

class TestCalculatorComprehensive:
    """Comprehensive test suite for the Calculator class."""
    
    # Addition tests
    def test_add_list(self):
        """Test addition of multiple numbers."""
        calc = Calculator()
        assert calc.add([1.0, 2.0, 3.0]) == 6.0
        assert calc.add([]) == 0.0
        assert calc.add([-1.0, 1.0]) == 0.0
    
    def test_add_single_number(self):
        """Test addition with a single number."""
        calc = Calculator()
        assert calc.add([5.0]) == 5.0
        assert calc.add([0.0]) == 0.0
        assert calc.add([-3.0]) == -3.0
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        calc = Calculator()
        assert calc.add([-1.0, -2.0, -3.0]) == -6.0
        assert calc.add([-5.0, 5.0]) == 0.0
    
    def test_add_decimals(self):
        """Test addition with decimal numbers."""
        calc = Calculator()
        result = calc.add([1.5, 2.5, 3.0])
        assert abs(result - 7.0) < 0.0001
    
    def test_add_large_numbers(self):
        """Test addition with large numbers."""
        calc = Calculator()
        assert calc.add([1e10, 2e10]) == 3e10
    
    # Subtraction tests
    def test_subtract_list(self):
        """Test subtraction of multiple numbers."""
        calc = Calculator()
        # 10 - 2 - 3 = 5
        assert calc.subtract([10.0, 2.0, 3.0]) == 5.0
        # 10 - (-2) = 12
        assert calc.subtract([10.0, -2.0]) == 12.0
        assert calc.subtract([5.0]) == 5.0
        assert calc.subtract([]) == 0.0
    
    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        calc = Calculator()
        # -5 - (-3) = -2
        assert calc.subtract([-5.0, -3.0]) == -2.0
        # -10 - 5 = -15
        assert calc.subtract([-10.0, 5.0]) == -15.0
    
    def test_subtract_decimals(self):
        """Test subtraction with decimal numbers."""
        calc = Calculator()
        result = calc.subtract([10.5, 2.5, 1.0])
        assert abs(result - 7.0) < 0.0001
    
    def test_subtract_to_negative(self):
        """Test subtraction resulting in negative number."""
        calc = Calculator()
        assert calc.subtract([5.0, 10.0]) == -5.0
    
    # Power tests
    def test_power_positive_integers(self):
        """Test power with positive integers."""
        calc = Calculator()
        assert calc.power(2, 3) == 8
        assert calc.power(5, 2) == 25
        assert calc.power(10, 3) == 1000
    
    def test_power_zero_exponent(self):
        """Test power with zero exponent."""
        calc = Calculator()
        assert calc.power(5, 0) == 1
        assert calc.power(100, 0) == 1
        assert calc.power(0, 0) == 1
    
    def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        calc = Calculator()
        assert calc.power(2, -1) == 0.5
        assert calc.power(10, -2) == 0.01
    
    def test_power_fractional_exponent(self):
        """Test power with fractional exponent."""
        calc = Calculator()
        assert calc.power(4, 0.5) == 2.0  # Square root
        assert calc.power(27, 1/3) == 3.0  # Cube root
    
    def test_power_negative_base(self):
        """Test power with negative base."""
        calc = Calculator()
        assert calc.power(-2, 2) == 4
        assert calc.power(-2, 3) == -8
    
    # Modulus tests
    def test_modulus_positive_numbers(self):
        """Test modulus with positive numbers."""
        calc = Calculator()
        assert calc.modulus(10, 3) == 1
        assert calc.modulus(10, 5) == 0
        assert calc.modulus(7, 4) == 3
    
    def test_modulus_zero_remainder(self):
        """Test modulus when result is zero."""
        calc = Calculator()
        assert calc.modulus(10, 5) == 0
        assert calc.modulus(100, 10) == 0
    
    def test_modulus_negative_dividend(self):
        """Test modulus with negative dividend."""
        calc = Calculator()
        result = calc.modulus(-10, 3)
        # Python modulus behavior: -10 % 3 = 2
        assert result == 2
    
    def test_modulus_negative_divisor(self):
        """Test modulus with negative divisor."""
        calc = Calculator()
        result = calc.modulus(10, -3)
        # Python modulus behavior: 10 % -3 = -2
        assert result == -2
    
    def test_modulus_by_zero(self):
        """Test that modulus by zero raises ValueError."""
        calc = Calculator()
        with pytest.raises(ValueError, match="Cannot calculate modulus with zero divisor."):
            calc.modulus(10, 0)
    
    def test_modulus_decimal_numbers(self):
        """Test modulus with decimal numbers."""
        calc = Calculator()
        result = calc.modulus(10.5, 3.0)
        assert abs(result - 1.5) < 0.0001
    
    # Integration tests
    def test_chained_operations(self):
        """Test chaining multiple operations."""
        calc = Calculator()
        # (2^3) + 5 = 13
        power_result = calc.power(2, 3)
        add_result = calc.add([power_result, 5])
        assert add_result == 13
    
    def test_complex_calculation_workflow(self):
        """Test a complex workflow of operations."""
        calc = Calculator()
        # Calculate: (10 + 5) - 3
        sum_result = calc.add([10, 5])
        final_result = calc.subtract([sum_result, 3])
        assert final_result == 12
    
    # Boundary tests
    def test_very_large_list_addition(self):
        """Test addition with a large list of numbers."""
        calc = Calculator()
        numbers = list(range(1, 101))  # 1 to 100
        result = calc.add(numbers)
        assert result == 5050  # Sum of 1 to 100
    
    def test_precision_with_decimals(self):
        """Test floating point precision."""
        calc = Calculator()
        result = calc.add([0.1, 0.2])
        assert abs(result - 0.3) < 0.0001
    
    def test_mixed_integer_float_operations(self):
        """Test operations with mixed int and float types."""
        calc = Calculator()
        assert calc.add([1, 2.5, 3]) == 6.5
        assert calc.subtract([10, 2.5, 1.5]) == 6.0

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
