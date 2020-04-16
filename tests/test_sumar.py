from src.bingo import sumar
from src.bingo import restar

def test_sumar():
    assert sumar (1, 2) == 3

def test_restar():
    assert restar (3, 2) == 1
