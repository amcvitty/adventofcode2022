

def is_marker(bit):
    return len(set(bit)) == len(bit)


def find_message(input):
    return find_seq(input, 14)


def find_marker(input):
    return find_seq(input, 4)


def find_seq(input, l):
    for i in range(l, len(input)):
        if is_marker(input[i-l: i]):
            return i
    return 0
