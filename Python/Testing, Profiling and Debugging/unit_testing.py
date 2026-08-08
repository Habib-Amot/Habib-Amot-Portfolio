"""
PYTHON UNIT TESTING - EXPLANATORY COMMENTS
===========================================

Unit testing is a software testing method where individual units/components 
of a program are tested in isolation to verify they work as expected.

Python's built-in 'unittest' module provides:
- TestCase class: Base class for test cases
- Test discovery: Automatically finds and runs tests
- Assertions: Methods to check conditions
- Fixtures: Setup and teardown methods
"""

import unittest


# ============================================================================
# EXAMPLE: Simple function to test
# ============================================================================

def add_numbers(a, b):
    """Simple function that adds two numbers."""
    return a + b


def divide_numbers(a, b):
    """Divides two numbers. Raises ValueError if divisor is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# ============================================================================
# BASIC UNIT TEST CLASS
# ============================================================================

class TestMathOperations(unittest.TestCase):
    """
    Unit test class that inherits from unittest.TestCase.
    
    Any method that starts with 'test_' is automatically discovered
    and executed by the test runner.
    """
    
    # ------------------------------------------------------------------------
    # SETUP AND TEARDOWN METHODS (FIXTURES)
    # ------------------------------------------------------------------------
    
    def setUp(self):
        """
        setUp() runs BEFORE each test method.
        Use this to initialize test data or setup test environment.
        Example: Creating database connections, initializing variables.
        """
        self.test_value_1 = 5
        self.test_value_2 = 3
        print("\nRunning setUp() - preparing test environment")
    
    def tearDown(self):
        """
        tearDown() runs AFTER each test method.
        Use this to clean up resources created during tests.
        Example: Closing database connections, deleting temporary files.
        """
        print("Running tearDown() - cleaning up after test")
    
    # ------------------------------------------------------------------------
    # CLASS-LEVEL SETUP (runs once for entire class)
    # ------------------------------------------------------------------------
    
    @classmethod
    def setUpClass(cls):
        """
        setUpClass() runs ONCE before all test methods in the class.
        Use @classmethod decorator. Shared setup for expensive operations.
        """
        print("=" * 50)
        print("Setting up TestMathOperations class")
        print("=" * 50)
    
    @classmethod
    def tearDownClass(cls):
        """
        tearDownClass() runs ONCE after all test methods in the class.
        Use @classmethod decorator. Cleanup after all tests complete.
        """
        print("=" * 50)
        print("Tearing down TestMathOperations class")
        print("=" * 50)
    
    # ------------------------------------------------------------------------
    # TEST METHODS (must start with 'test_')
    # ------------------------------------------------------------------------
    
    def test_add_positive_numbers(self):
        """
        Test adding two positive numbers.
        Uses assertEqual() to verify expected result.
        """
        result = add_numbers(self.test_value_1, self.test_value_2)
        # assertEqual checks if two values are equal
        self.assertEqual(result, 8, "Adding 5 and 3 should equal 8")
    
    def test_add_negative_numbers(self):
        """
        Test adding negative numbers.
        Uses assertEqual() to check correct behavior with negatives.
        """
        result = add_numbers(-5, -3)
        self.assertEqual(result, -8)
    
    def test_divide_normal_case(self):
        """
        Test normal division operation.
        Uses assertAlmostEqual() for floating-point comparisons
        (avoids precision issues).
        """
        result = divide_numbers(10, 3)
        # assertAlmostEqual checks if values are approximately equal
        self.assertAlmostEqual(result, 3.333333, places=5)
    
    def test_divide_by_zero(self):
        """
        Test that dividing by zero raises an exception.
        Uses assertRaises() to verify exception is raised.
        """
        # assertRaises checks if a specific exception is raised
        with self.assertRaises(ValueError):
            divide_numbers(10, 0)
    
    def test_divide_by_zero_message(self):
        """
        Test exception message when dividing by zero.
        assertRaises can also check the exception message.
        """
        with self.assertRaises(ValueError) as context:
            divide_numbers(10, 0)
        
        # Check the exception message
        self.assertEqual(str(context.exception), "Cannot divide by zero")


# ============================================================================
# RUNNING TESTS
# ============================================================================

if __name__ == '__main__':
    """
    When you run this file directly, unittest.main() will:
    1. Discover all test classes (subclasses of unittest.TestCase)
    2. Discover all test methods (methods starting with 'test_')
    3. Run them and display results
    
    Run this file with: python unit_testing.py
    
    For verbose output: python unit_testing.py -v
    """
    unittest.main(verbosity=2)  # verbosity=2 shows detailed output
