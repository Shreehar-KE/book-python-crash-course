import pytest
from employee import Employee


@pytest.fixture
def employee():
    """An employee instance that will available to all test functions"""
    employee = Employee('Jordan', 'Belfort', 72000)
    return employee


def test_give_default_raise(employee):
    """verifies the salary with default raise"""
    # employee = Employee('John', 'Wick', 7000000)
    employee.give_raise()
    assert employee.salary == 77000


def test_give_custom_raise(employee):
    """verifies the salary with 8000 raise"""
    # employee = Employee('Jordan', 'Belfort', 72000)
    employee.give_raise(3000)
    assert employee.salary == 75000
