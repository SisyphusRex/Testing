"""Tests for Employee Module"""

# System Imports
from unittest import TestCase

# First Party Imports
from employee import HourlyEmployee, SalaryEmployee

# Third Party Imports


class HourlyEmployeeTest(TestCase):
    """Test for HourlyEmployee"""

    def setUp(self):
        """Set up method for all tests in this class"""
        self.hourly_employee = HourlyEmployee("Test", "User", 10.00, 50.00)

    def test_hourly_employee_creation(self):
        """Test hourly employee creation"""

        # Arrange
        # set things up for the test
        expected_first_name = "Test"
        expected_last_name = "User"
        expected_hourly_rate = 10.00
        expected_hous_per_week = 50.00

        # Act
        # do the action that is being tested
        # NOTE: you must rewrite the values here and not copy the variable name because of mutable data types
        # = HourlyEmployee("Test", "User", 10.00, 50.00)

        # Assert
        # verify that the the result is expected
        self.assertEqual(self.hourly_employee.first_name, expected_first_name)
        self.assertEqual(self.hourly_employee.last_name, expected_last_name)
        self.assertEqual(self.hourly_employee.hourly_rate, expected_hourly_rate)
        self.assertEqual(self.hourly_employee.hours_per_week, expected_hous_per_week)

    def test_hourly_employee_str_method(self):
        """Test hourly employee str method"""

        # Arrange
        expected = f"{'Test':<10} {'User':<20} {'$500.00':>14}"

        # Act
        actual = str(self.hourly_employee)

        # Assert
        self.assertEqual(actual, expected)

    def test_hourly_employee_formatted_yearly_salary(self):
        """Test hourly employee formatted yearly"""

        # arrange
        expected = "$26000.00"

        # Act
        actual = self.hourly_employee.formatted_yearly_salary

        # assert

        self.assertEqual(actual, expected)


class SalaryEmployeeTest(TestCase):
    """Test for HourlyEmployee"""

    def setUp(self):
        """Set up method for all tests in this class"""
        self.salary_employee = SalaryEmployee("Test", "User", 500.00)

    def test_salary_employee_creation(self):
        """Test hourly employee creation"""

        # Arrange
        # set things up for the test
        expected_first_name = "Test"
        expected_last_name = "User"
        expected_weekly_salary = 500.00

        # Act
        # do the action that is being tested
        # NOTE: you must rewrite the values here and not copy the variable name because of mutable data types
        # = HourlyEmployee("Test", "User", 10.00, 50.00)

        # Assert
        # verify that the the result is expected
        self.assertEqual(self.salary_employee.first_name, expected_first_name)
        self.assertEqual(self.salary_employee.last_name, expected_last_name)
        self.assertEqual(self.salary_employee.weekly_salary, expected_weekly_salary)

    def test_salary_employee_str_method(self):
        """Test hourly employee str method"""

        # Arrange
        expected = f"{'Test':<10} {'User':<20} {'$500.00':>14}"

        # Act
        actual = str(self.salary_employee)

        # Assert
        self.assertEqual(actual, expected)

    def test_salary_employee_formatted_yearly_salary(self):
        """Test hourly employee formatted yearly"""

        # arrange
        expected = "$26000.00"

        # Act
        actual = self.salary_employee.formatted_yearly_salary

        # assert

        self.assertEqual(actual, expected)
