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
        # variables for the gui to perform as expected
        self.tk = Tk()
        self.tk.title("Testing the title")
        self.load_buttons()
        self.m_vars = []
        self.l_vars = []

        # backend variables
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
        r = 0
        c0 = 0
        c1 = 1
        c2 = 2
        var1=StringVar(); var1.set(False)
        var2=StringVar(); var2.set(False)
        var3=StringVar(); var3.set(False)
        var4=StringVar(); var4.set(False)
        var5=StringVar(); var5.set(False)
        var6=StringVar(); var6.set(False)
        var7=StringVar(); var7.set(False)
        leg1=StringVar(); leg1.set(False)
        leg2=StringVar(); leg2.set(False)
        leg3=StringVar(); leg3.set(False)
        leg4=StringVar(); leg4.set(False)
        leg5=StringVar(); leg5.set(False)
        leg6=StringVar(); leg6.set(False)
        leg7=StringVar(); leg7.set(False)

        # row 1
        m_on1 = "MDate.formatDateShortYear"
        l_on1 = "Legacy.formatDateShortYear"
        Label(t, text="fna$").grid(row=r, column=c0, sticky=W)
        Checkbutton(t, text=m_on1, variable=var1, onvalue=m_on1, offvalue=None).grid(row=r, column=c1, sticky=W)
        Checkbutton(t, text=l_on1, variable=leg1, onvalue=l_on1, offvaleu=None).grid(row=r, column=c2, sticky=W)
        r += 1

        # row 2
        m_on2 = "MDate.formatDateLongYear"
        l_on2 = "Legacy.formatDateLongYear"
        Label(t, text="fnax$").grid(row=r, column=c0, sticky=W)
        Checkbutton(t, text=m_on2, variable=var2, onvalue=m_on2, offvalue=None).grid(row=r, column=c1, sticky=W)
        Checkbutton(t, text=l_on2, variable=leg2, onvalue=l_on2, offvalue=None).grid(row=r, column=c2, sticky=W)
        r += 1

        # row 3
        m_on3 = "MDate.formatDateMonthDay"
        l_on3 = "Legacy.formatDateMonthDay"
        Label(t, text="fnas$").grid(row=r, column=c0, sticky=W)
        Checkbutton(t, text=m_on3, variable=var3, onvalue=m_on3, offvalue=None).grid(row=r, column=c1, sticky=W)
        Checkbutton(t, text=l_on3, variable=leg3, onvalue=l_on3, offvalue=None).grid(row=r, column=c2, sticky=W)
        r += 1

        # row 4
        m_on4 = "MDate.unpackDate"
        l_on4 = "Legacy.unpackDate"
        Label(t, text="fnudate$").grid(row=r, column=c0, sticky=W)
        Checkbutton(t, text=m_on4, variable=var4, onvalue=m_on4, offvalue=None).grid(row=r, column=c1, sticky=W)
        Checkbutton(t, text=l_on4, variable=leg4, onvalue=l_on4, offvalue=None).grid(row=r, column=c2, sticky=W)
        r += 1

        # row 5
        m_on5 = "MDate.packDate"
        l_on5 = "Legacy.packDate"
        Label(t, text="fnpdate$").grid(row=r, column=c0, sticky=W)
        Checkbutton(t, text=m_on5, variable=var5, onvalue=m_on5, offvalue=None).grid(row=r, column=c1, sticky=W)
        Checkbutton(t, text=l_on5, variable=leg5, onvalue=l_on5, offvalue=None).grid(row=r, column=c2, sticky=W)
        r += 1

        # row 6
        m_on6 = "MHouse.packHouseNumber"
        l_on6 = "Legacy.packHouseNumber"
        Label(t, text="fnp$").grid(row=r, column=c0, sticky=W)
        Checkbutton(t, text=m_on6, variable=var6, onvalue=m_on6, offvalue=None).grid(row=r, column=c1, sticky=W)
        Checkbutton(t, text=l_on6, variable=leg6, onvalue=l_on6, offvalue=None).grid(row=r, column=c2, sticky=W)
        r += 1

        # row 7
        m_on7 = "MHouse.unpackHouseNumber"
        l_on7 = "Legacy.unpackHouseNumber"
        Label(t, text="fnu$").grid(row=r, column=c0, sticky=W)
        Checkbutton(t, text=m_on7, variable=var7, onvalue=m_on7, offvalue=None).grid(row=r, column=c1, sticky=W)
        Checkbutton(t, text=l_on7, variable=leg7, onvalue=l_on7, offvalue=None).grid(row=r, column=c2, sticky=W)
        r += 1

        # # process button
        Button(t, text="Add selected", command=lambda: self.add_selected([var1.get(),var2.get(),var3.get(),var4.get(),
                                                                          var5.get(),var6.get(),var7.get()],
                                                                         [leg1.get(),leg2.get(),leg3.get(),leg4.get(),
                                                                          leg5.get(),leg6.get(),leg7.get()]
                                                                        , t)).grid(row=r, column=c1, sticky=W)

    def add_selected(self, method_list: [str], functions_list: [str], win: Toplevel):
        # load values in the old code list
        self.load_old_list()
        print("MethodList: \n")
        i = 0
        for m, l in zip(method_list, functions_list):
            if m != "0":
                self.new_code_list.append(m)
            elif l != "0":
                self.new_code_list.append(l)
            else:
                self.old_code_list[i] = None
            i += 1
        win.destroy()

    def load_old_list(self):
        self.old_code_list = ["fna$", "fnax$", "fnas$", "fnudate$", "fnpdate$", "fnp$", "fnu$"]

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