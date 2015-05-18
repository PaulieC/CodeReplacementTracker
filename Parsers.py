# coding=utf-8
"""
This file is designed to hold the parsers that will be used to determine the current
value of a line and the following line state(s)
"""
__author__ = 'PaulieC'

# imports
import re
from CodeReplacementTracker.Parser import Parser
from CodeReplacementTracker.ParsedObjects import Window
from CodeReplacementTracker.ParsedObjects import Subroutine


class WindowParser(Parser):

    def __init__(self):
        super().__init__()
        self.window_list = [Window()]

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
        else:
            return False

    def state_0(self, line: str, line_num: int) -> bool:
        self.state = 0
        if self.window_name.match(line):
            self.state = 1
            window = Window()
            self.window_list.append(window)
            self.window_list[len(self.window_list) - 1].set_name(line)
            self.window_list[len(self.window_list) - 1].set_line_dec(line_num)
            print("Window current state:\t" + str(self.state))
            return True
        else:
            print("Window current state:\t" + str(self.state))
            return False


    def state_1(self, line: str, line_num: int) -> bool:
        """
        This state is true if the line is the heading for a window gui. This will move to state_2
        to search for the following lines if true.
        """
        if self.end_window.match(line):
            self.state = 3
            self.window_list[len(self.window_list) - 1].set_line_ret(line_num)
            print("Window current state:\t" + str(self.state))
            return True
        else:
            self.state = 2
            print("Window current state:\t" + str(self.state))
            self.state_2(line, line_num)

    def state_2(self, line: str, line_num: int) -> bool:
        """
        Checks the line to see if it matches any character strings that don't end the window.
        """
        if self.subroutine.match(line):
            self.window_list[len(self.window_list) - 1].add_gosub(line_num, line)
            print("Window current state:\t" + str(self.state))
            return True
        elif self.characters.match(line):
            print("Window current state:\t" + str(self.state))
            return True
        elif self.end_window.match(line):
            self.state = 3
            self.window_list[len(self.window_list) - 1].set_line_ret(line_num)
            print("Window current state:\t" + str(self.state))
            return True
        else:
            raise Exception("regex doesn't recognize this line: " + line)

    def state_3(self, line: str, line_num: int) -> bool:
        if self.window_name.match(line):
            self.state = 1
            window = Window()
            self.window_list.append(window)
            self.window_list[len(self.window_list) - 1].set_name(line)
            self.window_list[len(self.window_list) - 1].set_line_dec(line_num)
            print("Window current state:\t" + str(self.state))
            return True
        else:
            self.state = 0
            print("Window current state:\t" + str(self.state))
            return False

    def load_tokens(self) -> None:
        """
        window_name: Matches all strings that begin with W1 and end with :
        subroutine: Matches all strings that perform at least on subroutine call by invoking gosub subroutinename
        end_window: Matches any string that starts/ends with a series of spaces and is return
        characters: Matches all strings that do not begin with the whole word return. Case is ignored when
                    checking for matches.
        """
        self.window_name    = re.compile( "^\s*(?i)W1\w*:\s*$")
        self.subroutine     = re.compile(r"^.*(?i)gosub\b\s+.+$")
        self.end_window     = re.compile(r"^\s*(?i)return\b\s*$")
        self.characters     = re.compile(r"^(?i)(?!.*return\b).*$")

    def get_state(self) -> int:
        return self.state


class SubroutineParser(Parser):

    def __init__(self):
        super().__init__()
        self.subroutine_list = []

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
            subroutine = Subroutine()
            subroutine.set_name(line)
            subroutine.set_line_dec(line_num)
            self.subroutine_list.append(subroutine)
            self.state = 1
            print("Subroutine current state:\t" + str(self.state))
            return True
        else:
            print("Subroutine current state:\t" + str(self.state))
            return False

    def state_1(self, line: str, line_num: int) -> bool:
        if self.subroutine_name.match(line):
            self.state = 4
            print("Subroutine current state:\t" + str(self.state))
            return self.subroutine_list[len(self.subroutine_list) - 1].add_subroutine(line_num, line)
        elif self.end_routine.match(line):
            self.state = 3
            print("Subroutine current state:\t" + str(self.state))
            return self.subroutine_list[len(self.subroutine_list) - 1].set_line_ret(line_num)
        else:
            self.state = 2
            print("Subroutine current state:\t" + str(self.state))
            return self.sort_characters(line, line_num)


    def state_2(self, line: str, line_num: int) -> bool:
        if self.end_routine.match(line):
            self.state = 3
            print("Subroutine current state:\t" + str(self.state))
            return self.subroutine_list[len(self.subroutine_list) - 1].set_line_ret(line_num)
        elif self.subroutine_name.match(line):
            self.state = 4
            print("Subroutine current state:\t" + str(self.state))
            return self.subroutine_list[len(self.subroutine_list) - 1].add_subroutine(line_num, line)
        else:
            print("Subroutine current state:\t" + str(self.state))
            return self.sort_characters(line, line_num)

    def state_3(self, line: str, line_num: int) -> bool:
        if self.subroutine_name.match(line):
            self.state = 1
            subroutine = Subroutine()
            subroutine.set_name(line)
            subroutine.set_line_dec(line_num)
            self.subroutine_list.append(subroutine)
            self.state = 1
            print("Subroutine current state:\t" + str(self.state))
            return True
        elif self.end_routine.match(line):
            print("Subroutine current state:\t" + str(self.state))
            return True
        else:
            self.state = 0
            print("Subroutine current state:\t" + str(self.state))
            return False

    def state_4(self, line: str, line_num: int) -> bool:
        if self.end_routine.match(line):
            self.state = 3
            print("Subroutine current state:\t" + str(self.state))
            return self.subroutine_list[len(self.subroutine_list) - 1].set_line_ret(line_num)
        elif self.subroutine_name.match(line):
            print("Subroutine current state:\t" + str(self.state))
            return self.subroutine_list[len(self.subroutine_list) - 1].add_subroutine(line_num, line)
        else:
            self.state = 2
            print("Subroutine current state:\t" + str(self.state))
            return self.state_2(line, line_num)

    def sort_characters(self, line: str, line_num: int) -> bool:
        if self.gosub.match(line):
            return self.subroutine_list[len(self.subroutine_list) - 1].add_gosub(line_num, line)
        elif self.goto.match(line):
            return self.subroutine_list[len(self.subroutine_list) - 1].add_goto(line_num, line)
        elif self.exitto.match(line):
            return self.subroutine_list[len(self.subroutine_list) - 1].add_exit(line_num, line)
        else:
            return False

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
        end_routine: Matches any string that starts/ends with a series of spaces and is return, bye, release, or exit.
        """
        self.subroutine_name    = re.compile(r"^\s*(?i)(?!(gb_|W1).*)\w+:\s*$")
        self.characters         = re.compile(r"^(?i)(?!.*(return|bye|release|exit)\b).*$")
        self.gosub              = re.compile(r"^.*(?i)gosub\b.*$")
        self.goto               = re.compile(r"^.*(?i)goto\b.*$")
        self.exitto             = re.compile(r"^.*(?i)exitto\b.*$")
        self.end_routine        = re.compile(r"^\s*(?i)(return|bye|release|exit)\b\s*$")

    def get_state(self) -> int:
        return self.state