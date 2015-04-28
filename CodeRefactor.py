# coding=utf-8
"""

This is designed specifically for refactoring BBj code. Eclipse can perform a find/replace throughout a file but
the lines numbers are needed for code coverage purposes when tracking function calls.
The list of line numbers that the original line occurs on is printed under the replacement word(s) in the
destination file. It is suggested to use a .txt file for the simple format.
"""
__author__ = 'PaulieC'

# imports
import os

class CodeRefactor:
    """ Class to read through a file for select words and write out the line number that this word occurs on. """

    def __init__(self):
        self.old_code_list = []
        self.new_code_list = []
        self.replacement_dict = {}
        self.limit = -1
        self.path_list = ["", ""]

    def verify_directory(self, directory: str) -> bool:
        """
        Checks if the input directory exists on the system
        :param directory: str
        :return: bool
        """
        file_location_exists = os.path.exists(directory)
        return file_location_exists

    def request_directory(self, index: int) -> bool:
        """
        Requests a directory from the user and check if this directory exists.
        If it does, this directory is assigned to the class variable.
        :param index: int
        :return: bool
        """
        path_loc = input("Enter the directory\n"
                         "::  ")
        success = False
        if  self.verify_directory(path_loc):
            print("Using location: " + path_loc)
            self.path_list[index] = path_loc
            success = True
        else:
            print("The directory doesn't exist! Check your location and/or check your spelling.")
        return success

    def set_word_associations(self):
        """
        Accepts a limit value from the user and requests this amount of words
        for each list (old_code/new_code). The user has the option to overwrite
        these values should they decide to assign values again.
        """
        number_code = input("How many words should we search for?\n"
                            "::  ")
        try:
            number_code = int(number_code)
            if number_code > 0:
                if self.limit > 0:
                    overwrite = input("The limit has already been set. Overwrite this? (Y/N)\n"
                                      "::  ")
                    if overwrite.upper() == "Y":
                        self.replacement_dict = {}
                        self.old_code_list  =[]
                        self.new_code_list = []
                    else:
                        print("Understood. Leaving this limit alone.")
                        return
                self.limit = number_code
                try:
                    self.load_lists()
                    print("Success!!")
                except Exception:
                    print("There was a problem filling the list of old code. Try again.")
            else:
                print("The number of words must be at least 1.\n"
                      "Try again...")
        except ValueError:
            print("The number of words to find should be an integer.\n"
                  "Try again...")

    def load_lists(self):
        """
        Requests from the user the words find and what you plan
        to use to replace them with.
        """
        # load the old code list
        print("We will begin adding words for searching.\n"
              "WARNING!!\n"
              "         Be careful of your inputs. If you make a mistake, you will have to start over from the "
                        "beginning AFTER loading the rest of the words.\n"
              "         Also, this algorithm is designed for a case insensitive language.")
        for x in range(0, self.limit):
            print("Enter group number " + str(x + 1) + " of " + str(self.limit))
            old = input("Enter old code piece to be found\n"
                        "::  ")
            self.old_code_list.append(old)
            new = input("Enter what this code will be replaced with\n"
                        "::  ")
            self.new_code_list.append(new)
            # setup this dictionary key with a default array as its value
            key = new
            self.replacement_dict.setdefault(key, [])

    def process_words_in_directories(self):
        """
        Performs the work of finding the line occurrences of the old
        code value and saves the new code value to the dictionary with
        the associated line number.
        """
        if self.old_code_list and self.new_code_list:
            if self.path_list[0] and self.path_list[1]:
                print("Locating words in file of source directory...")
                try:
                    with open(self.path_list[0], "r") as in_file:
                        for line_num, line in enumerate(in_file, 1):
                            for i in range(self.limit):
                                old_line = self.old_code_list[i]
                                key = self.new_code_list[i]
                                if old_line.lower() in line.lower():
                                    ignore_string = "def " + old_line
                                    if not ignore_string.lower() in line.lower():
                                        self.replacement_dict[key].append(str(line_num))
                        in_file.close()
                    print("Writing out to destination file...")
                    try:
                        with open(self.path_list[1], "w") as out_file:
                            for key in self.replacement_dict:
                                out_file.write("%s::\n" % key)
                                print("%s::\n" % key)
                                items = self.replacement_dict.get(key)
                                for val in items:
                                    out_file.write("\t%s\n" % val)
                                    print("\t%s\n" % val)
                            out_file.close()
                    except FileNotFoundError:
                        print("ERROR: Original destination file wasn't found.\n"
                              "Physically check directory.")
                except FileNotFoundError:
                    print("ERROR: Original source file wasn't found.\n"
                          "Physically check directory.")
            else:
                print("The directories haven't been set and/or verified.\n"
                      "Run option 1 and/or 2.")
        else:
            print("The lists are empty. Run option 4 before trying to process.")

    def print_dict(self):
        for key in self.replacement_dict:
            value = self.replacement_dict.get(key)
            print(key + "::")
            for val in value:
                print("     " + val)

    def handle_selection(self, user_choice: int) -> bool:
        """
        Handles the selection choice of the user
        :param user_choice: int
        :return: bool
        """
        status = True
        if user_choice == 1:
            # request source directory from user
            if self.request_directory(0):
                print("Input the destination directory if you haven't set it yet.")
        elif user_choice == 2:
            # request destination directory from user
            if self.request_directory(1):
                print("Now input the source directory if you haven't set it yet.")
        elif user_choice == 3:
            # request text to replace
            self.set_word_associations()
        elif user_choice == 4:
            # process the lists
            self.process_words_in_directories()
        elif user_choice == 5:
            # quit the "menu"
            status = False
        else:
            print("This selection isn't in the menu.\n"
                  "Try again.")
        return status

    def print_all_lists(self):
        if self.limit > 0:
            for x in range(0, self.limit):
                print(self.old_code_list[x] + " :: " + self.new_code_list[x])
            self.print_dict()
        else:
            print("Your lists are empty at this time.\n"
                  "Run option 3 first.")

    def run_menu(self):
        """ Continuous loop for printing the menu """
        running = True
        try:
            while running:
                print("1.   Setup source directory")
                print("2.   Setup destination directory")
                print("3.   Create lists of find/replace code pieces")
                print("4.   Process with current settings")
                print("5.   Quit")
                user_choice = input("Make selection\n"
                                    "::  ")
                try:
                    user_choice = int(user_choice)
                except ValueError:
                    print("This choice must be an integer value. Try again...")
                running = self.handle_selection(user_choice)
                print()
        except Exception:
            print("Unknown error occurred.\n"
                  "Suggest running debugger.\n"
                  "\n"
                  "Quit Program (SUGGESTED)\n"
                  "::  ")

    def main(self):
        self.run_menu()