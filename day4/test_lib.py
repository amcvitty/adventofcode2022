from lib import *


def test_contains():
    assert contains(1, 10, 2, 5)


def test_contains2():
    assert not contains(1, 10, 2, 15)


def test_overlaps():
    assert overlaps(2, 10, 1, 15)
