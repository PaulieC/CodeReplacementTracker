# coding=utf-8
__author__ = 'PaulieC'

class Parser:

    def __init__(self):
        self.state = 0
        self.load_tokens()

    def parse(self, line: str, line_num: int) -> bool:
        return self.determine_state(line, line_num)

    def determine_state(self, line: str, line_num: int) -> int:
        pass

    def state_0(self, line: str, line_num: int) -> bool:
        pass

    def state_1(self, line: str, line_num: int) -> bool:
        pass

    def state_2(self, line: str, line_num: int) -> bool:
        pass

    def state_3(self, line: str, line_num: int) -> bool:
        pass

    def state_4(self, line: str, line_num: int) -> bool:
        pass

    def load_tokens(self) -> None:
        pass

    def get_state(self) -> int:
        return self.state