from lib import *


def test_one():
    with open("example.txt") as f:
        lines = f.readlines()
    p = Parser(lines)
    m = p.parse_monkey()
    assert m.items == [79, 98]
    assert m.op == '*'
    assert m.op2 == '19'
    assert m.div_by == 23
    assert m.if_true == 2
    assert m.if_false == 3

    assert m.inspect_one() == (500, 3)
    assert m.inspections == 1


def test_all():
    with open("example.txt") as f:
        lines = f.readlines()
    p = Parser(lines)
    ms = p.parse_all()
    assert len(ms) == 4
