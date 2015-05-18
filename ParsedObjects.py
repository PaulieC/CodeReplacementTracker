# coding=utf-8
__author__ = 'PaulieC'

# imports
from CodeReplacementTracker.ParserDataStructure import ParserDataStructure

class Window(ParserDataStructure):

    def __init__(self):
        super().__init__()

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
            return True
        except Exception:
            return False

class Subroutine(ParserDataStructure):

    def __init__(self):
        super().__init__()
        self.subroutine_list = []

    def set_line_ret(self, num: int) -> bool:
        try:
            self.line_end = num
            if self.subroutine_list:
                self.subroutine_list[len(self.subroutine_list) - 1].set_line_ret(num - 1)
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
                    if self.subroutine_list:
                        self.subroutine_list[len(self.subroutine_list) - 1].add_gosub(line, val)
                    else:
                        self.gosub_lines.append([line, temp[0]])
                to_split = new_line[1]
            return True
        except Exception:
            return False

    def add_goto(self, line: int, val: str) -> bool:
        try:
            to_split = val
            new_line = [-1]
            while new_line:
                new_line = to_split.split(" ", 1)
                if new_line[0].lower() == "goto":
                    temp = new_line[1].split(" ", 1)
                    if self.subroutine_list:
                        self.subroutine_list[len(self.subroutine_list) - 1].add_goto(line, val)
                    else:
                        self.goto_lines.append([line, temp[0]])
                to_split = new_line[1]
            return True
        except Exception:
            return False

    def add_exit(self, line: int, val: str) -> bool:
        try:
            to_split = val
            new_line = [-1]
            while new_line:
                new_line = to_split.split(" ", 1)
                if new_line[0].lower() == "exitto":
                    temp = new_line[1].split(" ", 1)
                    if self.subroutine_list:
                        self.subroutine_list[len(self.subroutine_list) - 1].add_exit(line, val)
                    else:
                        self.goto_lines.append([line, temp[0]])
                to_split = new_line[1]
            return True
        except Exception:
            return False

    def add_subroutine(self, line: int, val: str) -> bool:
        subroutine = Subroutine()
        subroutine.set_name(val)
        subroutine.set_line_dec(line)
        if self.subroutine_list:
            self.subroutine_list[len(self.subroutine_list) - 1].set_line_ret(line - 1)
        self.subroutine_list.append(subroutine)
        return True