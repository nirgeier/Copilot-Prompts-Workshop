import pytest
from calculator.calculator import Calculator

class TestAdvancedCalculator:
    """Advanced test scenarios for Calculator operations."""
    
    # Power operation advanced tests
    def test_power_basic(self):
        """Test basic power operations."""
        calc = Calculator()
        assert calc.power(2, 3) == 8
        assert calc.power(5, 0) == 1
        assert calc.power(2, -1) == 0.5
    
    def test_power_edge_cases(self):
        """Test edge cases for power operations."""
        calc = Calculator()
        # Zero to positive power
        assert calc.power(0, 5) == 0
        # One to any power
        assert calc.power(1, 100) == 1
        # Large exponents
        assert calc.power(2, 10) == 1024
    
    def test_power_fractional_bases(self):
        """Test power with fractional bases."""
        calc = Calculator()
        assert abs(calc.power(0.5, 2) - 0.25) < 0.0001
        assert abs(calc.power(1.5, 2) - 2.25) < 0.0001
    
    # Modulus operation advanced tests
    def test_modulus_basic(self):
        """Test basic modulus operations."""
        calc = Calculator()
        assert calc.modulus(10, 3) == 1
        assert calc.modulus(10, 5) == 0
    
    def test_modulus_by_zero(self):
        """Test that modulus by zero raises ValueError."""
        calc = Calculator()
        with pytest.raises(ValueError, match="Cannot calculate modulus with zero divisor."):
            calc.modulus(10, 0)
    
    def test_modulus_with_floats(self):
        """Test modulus with floating point numbers."""
        calc = Calculator()
        result = calc.modulus(10.7, 3.2)
        assert abs(result - 1.1) < 0.0001
    
    def test_modulus_negative_combinations(self):
        """Test modulus with various negative number combinations."""
        calc = Calculator()
        # Both negative
        assert calc.modulus(-10, -3) == -1
        # Negative dividend, positive divisor
        assert calc.modulus(-10, 3) == 2
        # Positive dividend, negative divisor
        assert calc.modulus(10, -3) == -2
    
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
    
    def test_operations_with_previous_results(self):
        """Test using results from one operation in another."""
        calc = Calculator()
        # Start with addition
        sum_val = calc.add([2, 3, 5])  # 10
        # Use in power
        power_val = calc.power(sum_val, 2)  # 100
        # Use in modulus
        mod_val = calc.modulus(power_val, 7)  # 2
        assert mod_val == 2
    
    # Boundary and stress tests
    def test_very_large_list_addition(self):
        """Test addition with a large list of numbers."""
        calc = Calculator()
        numbers = list(range(1, 101))  # 1 to 100
        result = calc.add(numbers)
        assert result == 5050  # Sum of 1 to 100
    
    def test_very_large_list_subtraction(self):
        """Test subtraction with a large list."""
        calc = Calculator()
        numbers = [1000] + [1] * 100  # 1000 - 1 - 1 - ... (100 times)
        result = calc.subtract(numbers)
        assert result == 900
    
    def test_precision_with_decimals(self):
        """Test floating point precision issues."""
        calc = Calculator()
        # Test that can handle typical floating point arithmetic
        result = calc.add([0.1, 0.2])
        assert abs(result - 0.3) < 0.0001
    
    def test_mixed_integer_float_operations(self):
        """Test operations with mixed int and float types."""
        calc = Calculator()
        assert calc.add([1, 2.5, 3]) == 6.5
        assert calc.subtract([10, 2.5, 1.5]) == 6.0