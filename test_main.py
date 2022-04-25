from helpers import addition, subtraction, multiplication, division


def test_addition():
    assert addition(2, 2) == 4
    assert addition(2000, 20) == 2020
    assert addition(648, 2) == 650
    assert addition(12002, 2) == 12004
    assert addition(9876, 3) == 9879


def test_subtraction():
    assert subtraction(20, 5) == 15
    assert subtraction(200, 20) == 180
    assert subtraction(648, 2) == 646
    assert subtraction(90002, 2) == 90000
    assert subtraction(555, 3) == 552

def test_multiplication():
    assert multiplication(444, 5) == 2220
    assert multiplication(12345, 123) == 1518435
    assert multiplication(648, 2) == 1296
    assert multiplication(16422, 50000) == 821100000
    assert multiplication(555, 3) == 1665


def test_division():
    assert division(120, 6) == 20
    assert division(200, 20) == 10
    assert division(333, 3) == 111
    assert division(400000, 4) == 100000
    assert division(665544, 8) == 83193