import pytest


@pytest.fixture
def numbers():
    num_list = [1, 2, 3, 4, 5]
    yield num_list
    


def test_sum(numbers):
    total = sum(numbers)
    minium = min(numbers)
    maximum = max(numbers) 
    assert total == 15  
    assert minium == 1
    assert maximum == 5