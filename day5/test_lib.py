from lib import *


def test_parse():

    with open("example.txt") as f:
        lines = f.readlines()

    stacks, commands = parse(lines)
    s1, s2, s3 = stacks.s[1:4]
    assert s1 == ["Z", "N"]
    assert s2 == ["M", "C", "D"]
    assert s3 == ["P"]

    assert len(commands) == 4


def test_Stacks():
    stack = Stacks()
    stack.unshift(1, "D")
    stack.unshift(1, "C")
    assert stack.pop(1) == "D"


def test_stack_move():
    stacks = Stacks()
    stacks.push(1, "D")
    stacks.push(1, "E")
    stacks.move(1, 2)
    assert "E" == stacks.pop(2)
    assert "D" == stacks.pop(1)


def test_execute_command():
    stacks = Stacks()
    stacks.push(1, "D")
    stacks.push(1, "E")
    execute_command([2, 1, 2], stacks)
    assert "D" == stacks.pop(2)
    assert "E" == stacks.pop(2)


def test_parse_command():
    assert parse_command("move 11 from 2 to 1") == [11, 2, 1]
