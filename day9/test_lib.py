from lib import *


# .....    .....    .....
# .TH.. -> .T.H. -> ..TH.
# .....    .....    .....

def test_side_move(): assert new_tail(Point(3, 1), Point(1, 1)) == Point(2, 1)
def test_side_move2(): assert new_tail(Point(1, 1), Point(3, 1)) == Point(2, 1)
def test_up_move(): assert new_tail(Point(1, 3), Point(1, 1)) == Point(1, 2)


def test_stay(): assert new_tail(Point(1, 3), Point(1, 4)) == Point(1, 4)


def test_diag1(): assert new_tail(Point(2, 1), Point(0, 0)) == Point(1, 1)
def test_diag2(): assert new_tail(Point(-2, 1), Point(0, 0)) == Point(-1, 1)
def test_diag3(): assert new_tail(Point(-2, -1), Point(0, 0)) == Point(-1, -1)
def test_diag4(): assert new_tail(Point(2, -1), Point(0, 0)) == Point(1, -1)


def test_hash():
    assert len(set([Point(1, 2), Point(1, 2), Point(3, 3)])) == 2


def test_parse():
    assert (1, 0, 4) == parse("R 4")
