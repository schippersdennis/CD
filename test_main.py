from audioop import mul
from helpers import addition, subtraction, multiplication, division


def test_helpers():
    assert addition(2, 2) == 4
    assert subtraction(10, 5) == 5
    assert multiplication(60, 1000) == 60000
    assert division(700, 100) == 7
