__author__ = 'PaulieC'

# imports
import os
import fileinput
import re

class CodeRefactor:

    def __init__(self):
        self.old_code_list = []
        self.new_code_list = []
        self.replacement_dict = {}
        self.limit = -1
        self.path_list = ["", ""]

    def verify_directory(self, directory):
        file_location_exists = os.path.exists(directory)
        return file_location_exists

    def request_directory(self, index):
        path_loc = input("Enter the directory\n::  ")
        if  self.verify_directory(path_loc):
            print("Using location: " + path_loc)
            self.path_list[index] = path_loc
        else:
            print("The directory doesn't exist! Check your location and/or check your spelling.")
        return path_loc

    def set_word_amount(self):
        number_code = input("How many words should we search for?\n::  ")
        try:
            number_code = int(number_code)
            if number_code > 0:
                if self.limit > 0:
                    overwrite = input("The limit has already been set. Overwrite this? (Y/N)\n::  ")
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
                print("The number of words must be at least 1.\nTry again...")
        except ValueError:
            print("The number of words to find should be an integer.\nTry again...")

    def load_lists(self):
            # load the old code list
            print("We will begin adding words for searching.\n"
                  "WARNING!!\n"
                  "         Be careful of your inputs. If you make a mistake, you will have to start over from the "
                            "beginning AFTER loading the rest of the words.\n"
                  "         Also, this algorithm is designed for a case insensitive language.")
            for x in range(0, self.limit):
                print("Enter group number " + str(x + 1) + " of " + str(self.limit))
                old = input("Enter old code piece to be found\n::  ")
                self.old_code_list.append(old)
                new = input("Enter what this code will be replaced with\n::  ")
                self.new_code_list.append(new)
                # setup this dictionary key with a default array as its value
                key = new
                self.replacement_dict.setdefault(key, [])

    def process_words_in_directories(self):
        if self.old_code_list and self.new_code_list:
            if self.path_list:
                print("Locating words in file of source directory...")
                with open(self.path_list[0], "r") as in_file:
                    for line_num, line in enumerate(in_file, 1):
                        for i in range(self.limit):
                            old_line = self.old_code_list[i]
                            key = self.new_code_list[i]
                            if old_line.lower() in line.lower():
                                self.replacement_dict[key].append(str(line_num))
                    self.print_dict()
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

    def handle_selection(self, user_choice):
        status = True
        if user_choice == 1:
            # request source directory from user
            if self.request_directory(0):
                print("Now input the destination directory if you haven't set it yet.")
        elif user_choice == 2:
            # request destination directory from user
            if self.request_directory(1):
                print("Now input the destination directory if you haven't set it yet.")
        elif user_choice == 3:
            # request text to replace
            self.set_word_amount()
        elif user_choice == 4:
            # process the lists
            self.process_words_in_directories()
        elif user_choice == 5:
            # quit the "menu"
            status = False
        else:
            print("This selection isn't in the menu.\nTry again.")
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
        running = True
        while running:
            print("1.   Setup source directory")
            print("2.   Setup destination directory")
            print("3.   Create lists of find/replace code pieces")
            print("4.   Process with current settings")
            print("5.   Quit")
            user_choice = input("Make selection\n::  ")
            try:
                user_choice = int(user_choice)
            except ValueError:
                print("This choice must be an integer value. Try again...")
            running = self.handle_selection(user_choice)
            print()


    def main(self):
        self.run_menu()