"""
11-3. Employee: Write a class called Employee. The __init__() method should
take in a first name, a last name, and an annual salary, and store each of these
as attributes. Write a method called give_raise() that adds $5,000 to the
annual salary by default but also accepts a different raise amount.

      Write a test file for Employee with two test functions, test_give_default
_raise() and test_give_custom_raise(). Write your tests once without using a
fixture, and make sure they both pass. Then write a fixture so you don't have to
create a new employee instance in each test function. Run the tests again, and
make sure both tests still pass.
"""


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
