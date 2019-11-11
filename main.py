"""
Designed and created by Pourya Pooryeganeh
2018 Fall
"""
from library import *
from books import *
from persons import *
from view import *

class HomeView(View):
    def get_message(self, error=""):
        return """
    {}
    1. manage books
    2. manage persons
    3. manage cash

    your choose: """.format(error)

    def input_process(self, str_input):
        if str_input == "1":
            return ManageBook()
        
        elif str_input == "2":
            return ManagePerson()
        
        elif str_input == "3":
            return ManageCash()


def main():
    home = HomeView()

    home.enable()

main()
