from lib import *


def test_find_marker():
    assert find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert find_marker("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


def test_is_marker():
    assert is_marker("avsd")
    assert not is_marker("aa")
    assert not is_marker("aweoa")
