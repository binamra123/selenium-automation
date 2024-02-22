import pytest


@pytest.mark.parametrize("a, b, final", [(2, 6, 8), (5, 4, 9), (5, 10, 15)])

def testAdd(a, b, final):
    assert a + b == final