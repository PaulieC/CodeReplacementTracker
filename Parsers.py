# coding=utf-8
"""
This file is designed to hold the parsers that will be used to determine the current
value of a line and the following line state(s)
"""
__author__ = 'PaulieC'

# imports
import re


class window_parser:

    def __init__(self):
        self.curr_state = -1
        self.window_list = []
        self.window_tokens = []
        self.load_tokens()

    def window_parse(self, line: str) -> bool:
        pass

    def state(self, line: str) -> int:
        pass

    def load_tokens(self) -> None:
        window_name = re.compile("W" + "\w*\W*" + ":" )
        subroutine = re.compile("gosub" + "\s*\w*\W*")
        self.window_tokens = [window_name, subroutine]