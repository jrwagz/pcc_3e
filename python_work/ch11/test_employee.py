"""Pytest of employee module"""

from employee import Employee
import pytest

DEFAULT_SALARY = 60000.0
DEFAULT_RAISE = 5000.0


@pytest.fixture
def given_employee() -> Employee:
    """Create an Employee object to be used by tests"""
    return Employee(first_name="Joe", last_name="Smith", annual_salary=DEFAULT_SALARY)


def test_default_raise(given_employee: Employee) -> None:  # pylint: disable=redefined-outer-name
    """Test the behavior of a default raise"""
    given_employee.give_raise()
    assert given_employee.annual_salary == DEFAULT_SALARY + DEFAULT_RAISE


def test_custom_raise(given_employee: Employee) -> None:  # pylint: disable=redefined-outer-name
    """Test the behavior of a custom raise"""
    given_employee.give_raise(0.50)
    assert given_employee.annual_salary == DEFAULT_SALARY + 0.50
