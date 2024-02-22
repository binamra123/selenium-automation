import pytest


@pytest.fixture(params=[(2, 3), (5, 5), (10, 0)])  
def numbers(request):
    return request.param  

def test_addition(numbers):
    num1, num2 = numbers
    result = num1 + num2
    assert result > 0

def test_subtraction(numbers):
    num1, num2 = numbers
    result = num1 - num2
    assert result >= 0