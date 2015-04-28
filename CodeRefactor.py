__author__ = 'PaulieC'

# imports
import os

class CodeRefactor:

    def __init__(self):
        self.old_code_list = []
        self.new_code_list = []
        self.path_list = []

    def verify_directory(self, directory):
        file_location_exists = os.path.exists(directory)
        return file_location_exists

    def request_directory(self, index):
        path_loc = input("Enter the directory: ")
        if  self.verify_directory(path_loc):
            print("Using location: " + path_loc)
            self.path_list[index] = path_loc
            path_loc
        else:
            print("The directory doesn't exist! Try again and/or check your spelling.")
            return path_loc
    def run_menu(self):
        while True:
            # request source directory from user
            print("1.   Setup source directory")
            # request destination directory from user
            print("2.   Setup destination directory")
            # request text to replace
            print("3.   Load text to be replaced")
            # request text to overwrite old code
            print("4.   Load text for replacement")
            # run with settings
            print("5.   Process with current settings")
            # quit this "menu"
            print("6.   Quit")
            user_choice = input("Make selection: ")
            if user_choice == 1:
                pass
            elif user_choice == 2:
                pass
            elif user_choice == 3:
                pass
            elif user_choice == 4:
                pass
            elif user_choice == 5:
                pass
            elif user_choice == 6:
                break


    def main(self):
        print(self.verify_directory("hello"))