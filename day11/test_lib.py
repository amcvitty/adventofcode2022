from lib import *


def test_all():
    with open("example.txt") as f:
        lines = f.readlines()
    p = Parser(lines)
    ms = p.parse_all()
    assert len(ms) == 4
    m = ms[0]

    assert m.op == '*'
    assert m.op2 == '19'
    assert m.div_by == 23
    assert m.if_true == 2
    assert m.if_false == 3

    _item, next_monkey = m.inspect_one()
    assert next_monkey == 3
    assert m.inspections == 1


def test_item():
    i = Item(15, [3, 7])
    assert i.div_by(3)
    assert not i.div_by(7)
    i.add(13)  # now 28
    assert i.div_by(7)
    assert not i.div_by(3)
    i.mult(6)
    assert i.div_by(3)
