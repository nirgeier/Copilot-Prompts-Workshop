import pytest
from unittest.mock import patch, MagicMock
import sys
import os

# Add calculator directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'calculator'))

from cli_calculator import get_numbers_list, get_number

class TestCLIHelpers:
    """Test suite for CLI calculator helper functions."""
    
    def test_get_number_valid_input(self):
        """Test get_number with valid numeric input."""
        with patch('builtins.input', return_value='42'):
            result = get_number("Enter a number: ")
            assert result == 42.0
    
    def test_get_number_float_input(self):
        """Test get_number with float input."""
        with patch('builtins.input', return_value='3.14'):
            result = get_number("Enter a number: ")
            assert abs(result - 3.14) < 0.0001
    
    def test_get_number_negative_input(self):
        """Test get_number with negative number."""
        with patch('builtins.input', return_value='-5.5'):
            result = get_number("Enter a number: ")
            assert result == -5.5
    
    def test_get_number_invalid_then_valid(self):
        """Test get_number retries on invalid input."""
        with patch('builtins.input', side_effect=['invalid', '10']):
            with patch('builtins.print') as mock_print:
                result = get_number("Enter a number: ")
                assert result == 10.0
                mock_print.assert_called_with("Invalid input. Please enter a numeric value.")
    
    def test_get_numbers_list_space_separated(self):
        """Test get_numbers_list with space-separated values."""
        with patch('builtins.input', return_value='1 2 3 4 5'):
            result = get_numbers_list("Enter numbers: ")
            assert result == [1.0, 2.0, 3.0, 4.0, 5.0]
    
    def test_get_numbers_list_comma_separated(self):
        """Test get_numbers_list with comma-separated values."""
        with patch('builtins.input', return_value='1,2,3,4,5'):
            result = get_numbers_list("Enter numbers: ")
            assert result == [1.0, 2.0, 3.0, 4.0, 5.0]
    
    def test_get_numbers_list_mixed_separators(self):
        """Test get_numbers_list with mixed separators."""
        with patch('builtins.input', return_value='1, 2, 3 4, 5'):
            result = get_numbers_list("Enter numbers: ")
            assert result == [1.0, 2.0, 3.0, 4.0, 5.0]
    
    def test_get_numbers_list_single_number(self):
        """Test get_numbers_list with a single number."""
        with patch('builtins.input', return_value='42'):
            result = get_numbers_list("Enter numbers: ")
            assert result == [42.0]
    
    def test_get_numbers_list_floats(self):
        """Test get_numbers_list with floating point numbers."""
        with patch('builtins.input', return_value='1.5 2.5 3.5'):
            result = get_numbers_list("Enter numbers: ")
            assert result == [1.5, 2.5, 3.5]
    
    def test_get_numbers_list_negative_numbers(self):
        """Test get_numbers_list with negative numbers."""
        with patch('builtins.input', return_value='-1 -2 -3'):
            result = get_numbers_list("Enter numbers: ")
            assert result == [-1.0, -2.0, -3.0]
    
    def test_get_numbers_list_invalid_then_valid(self):
        """Test get_numbers_list retries on invalid input."""
        with patch('builtins.input', side_effect=['invalid input', '1 2 3']):
            with patch('builtins.print') as mock_print:
                result = get_numbers_list("Enter numbers: ")
                assert result == [1.0, 2.0, 3.0]
                mock_print.assert_called_with(
                    "Invalid input. Please enter numeric values separated by spaces or commas."
                )
    
    def test_get_numbers_list_mixed_valid_invalid(self):
        """Test get_numbers_list with partially invalid input."""
        with patch('builtins.input', side_effect=['1 two 3', '1 2 3']):
            with patch('builtins.print') as mock_print:
                result = get_numbers_list("Enter numbers: ")
                assert result == [1.0, 2.0, 3.0]
                mock_print.assert_called_with(
                    "Invalid input. Please enter numeric values separated by spaces or commas."
                )

class TestCLIIntegration:
    """Integration tests for CLI calculator main function."""
    
    def test_main_quit_immediately(self):
        """Test that main exits properly on 'quit' command."""
        with patch('builtins.input', return_value='quit'):
            with patch('builtins.print') as mock_print:
                from cli_calculator import main
                main()
                # Check that goodbye message was printed
                calls = [str(call) for call in mock_print.call_args_list]
                assert any('Goodbye' in str(call) for call in calls)
    
    def test_main_invalid_operation(self):
        """Test handling of invalid operation."""
        with patch('builtins.input', side_effect=['invalid_op', 'quit']):
            with patch('builtins.print') as mock_print:
                from cli_calculator import main
                main()
                # Check that error message was printed
                calls = [str(call) for call in mock_print.call_args_list]
                assert any('Unknown operation' in str(call) for call in calls)
    
    def test_main_addition_flow(self):
        """Test complete addition operation flow."""
        with patch('builtins.input', side_effect=['add', '1 2 3', 'quit']):
            with patch('builtins.print') as mock_print:
                from cli_calculator import main
                main()
                # Check that result was printed
                calls = [str(call) for call in mock_print.call_args_list]
                assert any('Result: 6' in str(call) for call in calls)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
