# coding=utf-8
"""
This file is designed to hold the parsers that will be used to determine the current
value of a line and the following line state(s)
"""
__author__ = 'PaulieC'

# imports
import re
from CodeReplacementTracker.ParsedObjects import Window
from CodeReplacementTracker.ParsedObjects import Subroutine


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

class SubroutineParser:

    def __init__(self):
        self.state = 0
        self.subroutine_list = []
        self.load_tokens()

    def parse(self, line: str, line_num: int) -> bool:
        return self.determine_state(line, line_num)

    def determine_state(self, line: str, line_num: int) -> int:
        # perform initial check for line
        if self.state   == 0:
            return self.state_0(line, line_num)
        elif self.state == 1:
            return self.state_1(line, line_num)
        elif self.state == 2:
            return self.state_2(line, line_num)
        elif self.state == 3:
            return self.state_3(line, line_num)
        elif self.state == 4:
            return self.state_4(line, line_num)
        else:
            return False

    def state_0(self, line: str, line_num: int) -> bool:
        self.state = 0
        if self.subroutine_name.match(line):
            return self.state_1(line, line_num)
        else:
            return False

    def state_1(self, line: str, line_num: int) -> bool:
        self.state = 1
        if self.subroutine_name.match(line):
            subroutine = Subroutine()
            subroutine.set_name(line)
            subroutine.set_line_dec(line_num)
            self.subroutine_list.append(subroutine)
            self.state = 4
            return True
        elif self.end_routine.match(line):
            return self.state_3(line, line_num)
        else:
            return self.state_2(line, line_num)

    def state_2(self, line: str, line_num: int) -> bool:
        self.state = 2
        if self.end_routine.match(line):
            return self.state_3(line, line_num)
        elif self.subroutine_name.match(line):
            self.subroutine_list[len(self.subroutine_list) - 1].add_subroutine(line_num, line)
            return self.state_4(line, line_num)
        elif self.gosub.match(line):
            return self.subroutine_list[len(self.subroutine_list) - 1].add_gosub(line_num, line)
        elif self.goto.match(line):
            return self.subroutine_list[len(self.subroutine_list) - 1].add_goto(line_num, line)
        elif self.exitto.match(line):
            return self.subroutine_list[len(self.subroutine_list) - 1].add_exit(line_num, line)
        else:
            return True

    def state_3(self, line: str, line_num: int) -> bool:
        self.state = 3
        if self.end_routine.match(line):
            self.subroutine_list[len(self.subroutine_list) - 1].set_line_ret(line_num)
            return True
        elif self.subroutine_name.match(line):
            return self.state_1(line, line_num)
        elif self.end_routine.match(line):
            return True
        else:
            return self.state_0(line, line_num)

    def state_4(self, line: str, line_num: int) -> bool:
        self.state = 4
        if self.end_routine.match(line):
            return self.state_3(line, line_num)
        elif self.subroutine_name.match(line):
            return self.subroutine_list[len(self.subroutine_list) - 1].add_subroutine(line_num, line)
        else:
            return self.state_2(line, line_num)

    def load_tokens(self) -> None:
        """
        subroutine_name: Matches all strings that can have any number of spaces/tabs, do not start with gb__, and must
                         end in a colon before any number of spaces/tabs. This will not match a colon by itself or
                         a colon with a number of spaces before it; it must have at least one character before the
                         colon.
        characters: Matches all strings that do not begin with the whole words: return, exit, bye, or release. Case is
                    ignored when checking for matches.
        gosub: Matches all strings that contain the whole word gosub. Case is ignored when checking for matches.
        goto: Matches all strings that contain the whole word goto. Case is ignored when checking for matches.
        exitto: Matches all strings that contain the whole word exitto. Case is ignored when checking for matches.
        end_routine: TODO
        """
        self.subroutine_name = re.compile(r"^\s*(?i)(?!gb__.*)\w+:\s*$")
        self.characters = re.compile(r"^(?i)(?!.*(return|bye|release|exit)\b).*$")
        self.gosub = re.compile(r"^.*(?i)gosub\b.*$")
        self.goto = re.compile(r"^.*(?i)goto\b.*$")
        self.exitto = re.compile(r"^.*(?i)exitto\b.*$")
        self.end_routine = re.compile(r"\s*(?i)return\b\s*")

    def get_state(self) -> int:
        return self.state