# coding=utf-8
__author__ = 'intern1'


class Window:

    def __init__(self):
        self.line_declared = -1
        self.line_returned = -1
        self.gosub_lines = []
        self.window_name = ""

    def set_line_dec(self, num: int) -> bool:
        try:
            self.line_declared = num
            return True
        except Exception:
            return False

    def set_line_ret(self, num: int) -> bool:
        try:
            self.line_returned = num
            return True
        except Exception:
            return False

    def add_gosub(self, line: int, val: str) -> bool:
        try:
            to_split = val
            new_line = [-1]
            while new_line:
                new_line = to_split.split(" ", 1)
                if new_line[0].lower() == "gosub":
                    temp = new_line[1].split(" ", 1)
                    self.gosub_lines.append([line, temp[0]])

                to_split = new_line[1]
        except Exception:
            return False

    def set_name(self, name: str) -> bool:
        try:
            self.window_name = name
            return True
        except Exception:
            return False