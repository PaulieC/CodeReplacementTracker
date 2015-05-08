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
from tkinter import *
from tkinter.filedialog import askopenfilename

class CodeRefactor:
    """ Class to read through a file for select words and write out the line number that this word occurs on. """

    def __init__(self):
        self.tk = Tk()
        self.tk.title("Testing the title")
        self.load_buttons()

        self.old_code_list = []
        self.new_code_list = []
        self.replacement_dict = {}
        self.limit = -1
        self.path_list = ["", ""]

    def load_buttons(self):
        self.source_dir_button = Button(self.tk, text="Assign Source File", command=lambda: self.request_directory(0))
        self.source_dir_button.pack()

        self.dest_dir_button = Button(self.tk, text="Assign Destination File", command=lambda: self.request_directory(1))
        self.dest_dir_button.pack()

        self.assign_replacement_button = Button(self.tk, text="Text Replacement", command=self.set_word_associations)
        self.assign_replacement_button.pack()



    def verify_directory(self, directory: str) -> bool:
        """
        Checks if the input directory exists on the system
        :param directory: str
        :return: bool
        """
        file_location_exists = os.path.exists(directory)
        return file_location_exists

    def request_directory(self, index: int) -> bool:
        path_loc = askopenfilename()
        success = False
        if  self.verify_directory(path_loc):
            print("Using location: " + path_loc)
            self.path_list[index] = path_loc
            success = True
        else:
            print("The directory doesn't exist! Check your location and/or check your spelling.")
        return success

    def set_word_associations(self):
        # number_code = input("How many words should we search for?\n"
        #                     "::  ")
        t = Toplevel()
        t.title("New Window")
        # row 1
        var1 = StringVar()
        legacy1 = StringVar()
        Label(t, text="fna$").grid(row=1, column=0, sticky=W)
        Checkbutton(t, text="MDate.formatDateShortYear", variable=var1).grid(row=1, column=1, sticky=W)
        Checkbutton(t, text="Legacy.formatDateShortYear", variable=legacy1).grid(row=1, column=2, sticky=W)
        # row 2
        var2 = StringVar()
        legacy2 = StringVar()
        Label(t, text="fnax$").grid(row=2, sticky=W)
        Checkbutton(t, text="MDate.formatDateLongYear", variable=var2).grid(row=2, column=1, sticky=W)
        Checkbutton(t, text="Legacy.formatDateLongYear", variable=legacy2).grid(row=2, column=2, sticky=W)
        # row 3
        var3 = StringVar()
        legacy3 = StringVar()
        Label(t, text="fnas$").grid(row=3, sticky=W)
        Checkbutton(t, text="MDate.formatDateMonthDay", variable=var3).grid(row=3, column=1, sticky=W)
        Checkbutton(t, text="Legacy.formatDateMonthDay", variable=legacy3).grid(row=3, column=2, sticky=W)
        # row 4
        var4 = StringVar()
        legacy4 = StringVar()
        Label(t, text="fnudate$").grid(row=4, sticky=W)
        Checkbutton(t, text="MDate.unpackDate", variable=var4).grid(row=4, column=1, sticky=W)
        Checkbutton(t, text="Legacy.unpackDate", variable=legacy4).grid(row=4, column=2, sticky=W)
        # row 5
        var5 = StringVar()
        legacy5 = StringVar()
        Label(t, text="fnpdate$").grid(row=5, sticky=W)
        Checkbutton(t, text="MDate.packDate", variable=var5).grid(row=5, column=1, sticky=W)
        Checkbutton(t, text="Legacy.packDate", variable=legacy5).grid(row=5, column=2, sticky=W)
        # row 6
        var6 = StringVar()
        legacy6 = StringVar()
        Label(t, text="fnp$").grid(row=6, sticky=W)
        Checkbutton(t, text="MHouse.packHouseNumber", variable=var6).grid(row=6, column=1, sticky=W)
        Checkbutton(t, text="Legacy.packHouseNumber", variable=legacy6).grid(row=6, column=2, sticky=W)
        # row 7
        var7 = StringVar()
        legacy7 = StringVar()
        Label(t, text="fnu$").grid(row=7, sticky=W)
        Checkbutton(t, text="MHouse.unpackHouseNumber", variable=var7).grid(row=7, column=1, sticky=W)
        Checkbutton(t, text="Legacy.unpackHouseNumber", variable=legacy7).grid(row=7, column=2, sticky=W)

    def load_lists(self):
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
                                    out_file.write("%s\n" % val)
                                    print("%s\n" % val)
                            out_file.close()
                        self.clear_dictionary()
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

    def clear_dictionary(self):
       for key in self.replacement_dict:
           self.replacement_dict[key] = []

    def print_dict(self):
        for key in self.replacement_dict:
            value = self.replacement_dict.get(key)
            print(key + "::")
            for val in value:
                print("     " + val)

    def handle_selection(self, user_choice: int) -> bool:
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
        self.tk.mainloop()
        # try:
        #     while running:
        #         print("1.   Setup source directory")
        #         print("2.   Setup destination directory")
        #         print("3.   Create lists of find/replace code pieces")
        #         print("4.   Process with current settings")
        #         print("5.   Quit")
        #         user_choice = input("Make selection\n"
        #                             "::  ")
        #         try:
        #             user_choice = int(user_choice)
        #         except ValueError:
        #             print("This choice must be an integer value. Try again...")
        #         running = self.handle_selection(user_choice)
        #         print()
        # except Exception:
        #     print("Unknown error occurred.\n"
        #           "Suggest running debugger.\n"
        #           "\n"
        #           "Quit Program (SUGGESTED)\n"
        #           "::  ")

    def main(self):
        self.run_menu()