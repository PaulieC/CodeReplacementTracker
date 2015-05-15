# coding=utf-8
"""
This file is designed to hold the parsers that will be used to determine the current
value of a line and the following line state(s)
"""
__author__ = 'PaulieC'

# imports
import re
from CodeReplacementTracker.ParsedObjects import Window


class WindowParser:

    def __init__(self):
        self.state = 0 # start state
        self.window_list = [Window()]
        self.load_tokens()

    def parse(self, line: str, line_num: int) -> bool:
        return self.determine_state(line, line_num)

    def determine_state(self, line: str, line_num: int) -> int:
        # perform initial check for line
        if self.state == 0:
            return self.state_0(line, line_num)
        elif self.state == 1:
            return self.state_1(line, line_num)
        elif self.state == 2:
            return self.state_2(line, line_num)
        elif self.state == 3:
            return self.state_3(line, line_num)
        else:
            return False

    def state_0(self, line: str, line_num: int) -> bool:
        if self.window_name.match(line):
            self.state = 1
            return self.state_1(line, line_num)
        else:
            return False


    def state_1(self, line: str, line_num: int) -> bool:
        """
        This state is true if the line is the heading for a window gui. This will move to state_2
        to search for the following lines if true.
        """
        if self.window_name.match(line):
            # we are in a window block so initialize a window here and add it to the list
            window = Window()
            self.window_list.append(window)
            self.window_list[len(self.window_list) - 1].set_name(line)
            self.window_list[len(self.window_list) - 1].set_line_dec(line_num)
            return True
        elif self.subroutine.match(line) or self.characters.match(line):
            return self.state_2(line, line_num)
        elif self.end_window.match(line):
            return self.state_3(line, line_num)
        else:
            return False

    def state_2(self, line: str, line_num: int) -> bool:
        """
        Checks the line to see if it matches any character strings that don't end the window.
        """
        self.state = 2
        if self.subroutine.match(line):
            self.window_list[len(self.window_list) - 1].add_gosub(line_num, line)
            return True
        elif self.characters.match(line):
            return True
        elif self.end_window.match(line):
            return self.state_3(line, line_num)
        else:
            raise Exception("regex doesn't recognize this line: " + line)

    def state_3(self, line: str, line_num: int) -> bool:
        self.state = 3
        if self.end_window.match(line):
            self.window_list[len(self.window_list) - 1].set_line_ret(line_num)
            return True
        elif self.window_name.match(line):
            return self.state_1(line, line_num)
        else:
            self.state = 0
            return False

    def load_tokens(self) -> None:
        self.window_name    = re.compile("W" + "\w*\W*" + ":" ) # match string that starts with W and ends with :
        self.subroutine     = re.compile("[\w + \W]*" + "(?i)gosub" + "[\s + \w + \W]*") # match string that contain gosub
        self.end_window     = re.compile("(?i)return\s*")       # match string that is only a return
        self.characters     = re.compile("(?i)(?!return)^.*")   # match any character that doesn't start with return

    def get_state(self) -> int:
        return self.state