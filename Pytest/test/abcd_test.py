import pytest
#from Pytest.Source.math import math
import sys
#sys.path.insert(1, 'D:\QA Intern\Python basics\Pytest\Source\abcd.py')
#import Source.math as math
import Pytest.Sources.abcd as abcd


def test_add():
    result = abcd.add(number_one = 2, number_two= 5) 
    assert result == 7

def test_div():
    result = abcd.divide(number_one =5, number_two=5)
    assert result == 1