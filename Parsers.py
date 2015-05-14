# coding=utf-8
"""
This file is designed to hold the parsers that will be used to determine the current
value of a line and the following line state(s)
"""
__author__ = 'PaulieC'

# imports
import re
from CodeReplacementTracker.ParsedObjects import Window


class window_parser:

    def __init__(self):
        self.state = -1
        self.window_list = [Window()]
        self.load_tokens()

    def parse(self, line: str) -> bool:
        self.determine_state(line)

    def determine_state(self, line: str) -> int:
        # perform initial check for line
        if self.state == -1:
            window = Window()
            self.window_list.append(window)
            return self.state_1(line)
        elif self.state == 2:
            return self.state_2(line)
        else:
            return False

    def state_1(self, line: str) -> bool:
        """
        This state is true if the line is the heading for a window gui. This will move to state_2
        to search for the following lines if true.
        """
        if self.window_name.match(line):
            self.window_list[len(self.window_list) - 1].set_name(line)
            self.window_list[len(self.window_list) - 1].set_line_dec(line.getNumber())  # TODO handle line.
            self.state = 2
            return True
        else:
            return False

    def state_2(self, line: str) -> bool:
        """
        Checks the line to see if it matches any character strings that don't end the window.
        """
        if self.subroutine.match(line):
            self.window_list[len(self.window_list) - 1].add_gosub(line.getNumber(), line)   # TODO handle line.
            self.state = 2  # stay in state 2
            return True
        elif self.blank.match(line):
            # read past blank line
            return True
        elif self.end_window.match(line):
            # this is the end of the window block
            return self.state_3(line)
        elif self.characters.match(line):
            # this line is a string we don't care about and we should read past it
            return True
        else:
            raise Exception("regex doesn't recognize this line: " + line)

    def state_3(self, line: str) -> bool:
        # this is the end of the block so assign final value and clear class state
        self.window_list[len(self.window_list) - 1].set_line_ret(line.getNumber())  # TODO handle line.
        self.state = -1
        return False

    def load_tokens(self) -> None:
        self.window_name = re.compile("W" + "\w*\W*" + ":" )
        self.subroutine = re.compile("gosub" + "\s*\w*\W*")
        self.end_window = re.compile("(?i)return\s*")
        self.blank = re.compile("\s*")
        self.characters = re.compile("[\w + \W + \s]*")