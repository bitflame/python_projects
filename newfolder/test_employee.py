from employee import Employee
import pytest

@pytest.fixture
def employee():
    employee = Employee('Shahin', 'Ansari', 125000)
    return employee

def test_give_default_raise(employee):
    assert employee.give_raise(0) == 130000
    
def test_give_custom_raise(employee):
    assert employee.give_raise(3000) == 128000