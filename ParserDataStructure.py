# coding=utf-8
__author__ = 'PaulieC'


class ParserDataStructure:
    def __init__(self):
        self.line_declared = -1
        self.line_end = -1
        self.gosub_lines = []
        self.goto_lines = []
        self.exitto_lines = []
        self.name = ""

    def set_line_dec(self, num: int) -> bool:
        try:
            self.line_declared = num
            return True
        except Exception:
            return False

    def set_line_ret(self, num: int) -> bool:
        pass

    def add_gosub(self, line: int, val: str) -> bool:
        pass

    def add_goto(self, line: int, val: str) -> bool:
        pass

    def add_exit(self, line: int, val: str) -> bool:
        pass

    def add_subroutine(self, line: int, val: str) -> bool:
        pass

    def set_name(self, name: str) -> bool:
        self.name = name.strip().replace("\n", "").replace(":", "")
        return True