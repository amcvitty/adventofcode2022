import re


class Parser():
    def __init__(self, lines):
        self.lines = lines
        self.ptr = 0
        self.total = 0
        self.dirs = []

    def parse_ls(self):
        files = []
        dirs = []
        while(self.has_more() and self.peek_line()[0] != "$"):
            line = self.get_line()
            a, b = re.search(r'(\w+) ([A-Za-z.]+)', line).groups()
            if a == "dir":
                dirs.append(b)
            else:
                files.append(File(b, int(a)))

        return dirs, files

    def parse_directory(self, expected_name):
        line = self.get_line()
        print(line)
        dir_name = re.search(r'\$ cd (\S+)', line).groups()[0]
        if dir_name != expected_name:
            print(f"expected directory {expected_name} but got {dir_name}")
            exit(1)
        self.expect_line(r'\$ ls')
        dirs, files = self.parse_ls()

        dirs = [self.parse_directory(dirname) for dirname in dirs]
        if self.has_more():
            self.expect_line(r'\$ cd ..')
        d = Directory(dir_name, files + dirs)
        self.record_dir(d)
        return d

    def record_dir(self, d):
        self.dirs.append(d)

    def expect_line(self, exp):
        assert re.match(exp, self.get_line())

    def get_line(self):
        line = self.lines[self.ptr]
        self.ptr += 1
        return line

    def peek_line(self):
        return self.lines[self.ptr]

    def has_more(self):
        return self.ptr < len(self.lines)


class Directory:
    def __init__(self, name, entries=[]):
        self.entries = entries
        self.name = name

    def set_entries(self, entries):
        self.entries = entries

    def get_size(self):
        return sum([e.get_size() for e in self.entries])


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size
