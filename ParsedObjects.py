# coding=utf-8
__author__ = 'intern1'


class window:

    def __init__(self):
        self.line_declared = -1
        self.line_returned = -1
        self.gosub_lines = {}
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

    def add_gosub(self, key: int, val: str) -> bool:
        try:
            if key in self.gosub_lines:
                return False
            else:
                self.gosub_lines[key] = val
                return True
        except Exception:
            return False

    def set_name(self, name: str) -> bool:
        try:
            self.window_name = name
            return True
        except Exception:
            return False