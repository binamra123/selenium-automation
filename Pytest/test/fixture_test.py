import pytest

@pytest.fixture
def setup_data():
    data = {
        'x': 10,
        'y': 5
    }
    return data

def test_multiplication(setup_data):
    multiply = getattr(__import__('math_operations'), 'multiply')
    result = multiply(setup_data['x'], setup_data['y'])
    assert result == 50

def test_division(setup_data):
    divide = getattr(__import__('math_operations'), 'divide')
    result = divide(setup_data['x'], setup_data['y'])
    assert result == 2.0 

def test_addition(setup_data):
    add = getattr(__import__('math_operations'), 'add')
    result = add(setup_data['x'], setup_data['y'])
    assert result == 15

def test_subtraction(setup_data):
    subtract = getattr(__import__('math_operations'), 'subtract')
    result = subtract(setup_data['x'], setup_data['y'])
    assert result == 5