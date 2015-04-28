__author__ = 'PaulieC'

# imports
import os

class CodeRefactor:

    def __init__(self):
        self.old_code_list = []
        self.new_code_list = []
        self.limit = -1
        self.path_list = []

    def verify_directory(self, directory):
        file_location_exists = os.path.exists(directory)
        return file_location_exists

    def request_directory(self, index):
        path_loc = input("Enter the directory: ")
        if  self.verify_directory(path_loc):
            print("Using location: " + path_loc)
            self.path_list[index] = path_loc
        else:
            print("The directory doesn't exist! Check your location and/or check your spelling.")
        return path_loc

    def set_word_amount(self):
        number_code = input("How many words should we replace?")
        try:
            number_code = int(number_code)
            if number_code > 0:
                if self.limit > 0:
                    overwrite = input("The limit has already been set. Overwrite this? (Y/N):")
                    if overwrite.upper() == "Y":
                        pass
                    else:
                        print("Understood. Leaving this limit alone.")
                        return
                self.limit = number_code
                loaded_lists = self.load_lists()
                try:
                    print("Success!!")
                except Exception:
                    print("There was a problem filling the list of old code. Try again.")
            else:
                print("The number of words must be at least 1.\nTry again...")
        except ValueError:
            print("The number of words to replace should be an integer.\nTry again...")

    def load_lists(self):
            # load the old code list
            print("We will begin adding words for replacement.\n"
                  "WARNING!!\n"
                  "         Be careful of your inputs. If you make a mistake, you will have to start over from the "
                            "beginning after loading the rest of the words.\n"
                  "         Also, this algorithm is case insensitive.")
            for x in range(0, self.limit):
                print("Enter group number " + str(x) + " of " + str(self.limit))
                old = input("Enter old code piece to be replaced")
                self.old_code_list.append(old)
                new = input("Replace this piece with: ")
                self.new_code_list.append(new)

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
            # request text to overwrite old code
            self.print_all_lists()
        elif user_choice == 5:
            # run with settings
            status = False
        else:
            print("This selection isn't in the menu.\nTry again.")
        return status

    def print_all_lists(self):
        if self.limit > 0:
            for x in range(0, self.limit):
                print(self.old_code_list[x] + " :: " + self.new_code_list[x])
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
            user_choice = input("Make selection: ")
            try:
                user_choice = int(user_choice)
            except ValueError:
                print("This choice must be an integer value. Try again...")
            running = self.handle_selection(user_choice)
            print()


    def main(self):
        self.run_menu()