import os
from library import *
from books import *

class ItIsNotEnabled(Exception):
    pass

class View:
    stack = []
    #commands = ["Home"]

    def __init__(self, message=None):
        self.message = message
        self.error = ""

    def enable(self):
        os.system('cls')
        if self is not self.enabled_view():
            self.stack.append(self)

        print("\n\tType :help for help")
        #print("\t{}".format(' => '.join(self.commands)))
        if self.message == None:
            print(self.get_message(), end="")
        else:
            print(self.message, end="")
            
        inp = input()
        v = None
        if len(inp) > 0 and inp[0] == ":":
            v = View.input_process(self, inp[1:])
        else:
            v = self.input_process(inp)

        if v == None:
            self.message = self.get_message("!Invalid Input or Command!")
            self.enable()
            self.message = None
        else:
            #if inp != "back" and inp != ":back":
            #   self.commands.append(inp)
            v.enable()
        self.message = None

    def disable(self):
        if len(self.stack) == 1:
            return
        self.stack.pop()
        before = self.enabled_view()
        return before

    def input_process(self, str_input):
        if str_input == "help":
            return HelpView()
        elif str_input == "back":
            #self.commands.pop()
            return self.disable()
        elif str_input == "exit":
            exit()

    def error_view(self, error=""):
        self.message = self.get_message(error)
        return self

    def get_message(self, error=""):
        return ""

    @staticmethod
    def enabled_view():
        if len(View.stack) == 0:
            return None
        return View.stack[len(View.stack) - 1]

class HelpView(View):

    def get_message(self, error=""):
        return """
    {}
    help: show this message
    back: return to last page
    exit: exit program instantly

    NOTE: you must use ':' sign before above commands

    enter input: """.format(error)

class ManageBook(View):
    def input_process(self, str_input):
        if str_input == "1":
            return AddBook()
        
        elif str_input == "2":
            return ListBook()
        
        elif str_input == "3":
            return CountBook()

    def get_message(self, error=""):
        return """
    {}
    1. add books
    2. list books
    3. count of books

    your choose: """.format(error)

class AddBook(View):
    def input_process(self, str_input):
        str_input = str_input.split(" ")
        if len(str_input) == 3:
            try:
                name = str_input[0]
                publish_year = int(str_input[1])
                price = int(str_input[2])
                book = Book(name, publish_year, price)
                library.add_book(book)
                return self.error_view("#The book({}, {}, {}) has been added#".format(name, publish_year, price))
            except ValueError:
                return
    
    def get_message(self, error=""):
        return """
    {}
    Enter book_name(textWithOutSpace) publish_year(number) price(number)
    ex. book1 2012 2000

    Enter: """.format(error)

class ListBook(View):
    def get_message(self, error=""):
        return """
    {}

    {}
    > """.format(library.books_list_string(), error)


class CountBook(View):
    def get_message(self, error=""):
        return """
    {}
    {}

    > """.format(error, library.books.count)



class ManagePerson(View):
    def get_message(self, error=""):
        return """
    {}
    1. add man to queue
    2. add woman to queue
    3. add book for persons

    your choose: """.format(error)

    def input_process(self, str_input):
        if str_input == "1":
            return AddMan()
        
        elif str_input == "2":
            return AddWoman()
        
        elif str_input == "3":
            return Manage_one_Person()

class Manage_one_Person(View):
    def input_process(self, str_input):
        str_input = str_input.split(" ")
        if len(str_input) == 3:
            try:
                t = str_input[0]
                person_id = int(str_input[1])
                book_id = int(str_input[2])

                book_to_cart = library.books[book_id - 1]
                if book_to_cart == None:
                    return self.error_view("!Wrong book_id!")

                if t == "MEN":
                    if person_id - 1 >= len(library.men_queue):
                        return self.error_view("!Wrong person_id!")
                    b = book_to_cart.book
                    p = library.men_queue[person_id - 1]
                    p.add_to_cart(b)
                    libbooks = library.books
                    del library.books[book_id - 1]
                    libbooks.save(library.books_file)
                    return self.error_view("#The book({}) has been added to the cart of person({})#".format(b.name, p.name))

                elif t == "WOMEN":
                    if person_id - 1 >= len(library.women_queue):
                        return self.error_view("!Wrong person_id!")
                    b = book_to_cart.book
                    p = library.women_queue[person_id - 1]
                    p.add_to_cart(b)
                    libbooks = library.books
                    del library.books[book_id - 1]
                    libbooks.save(library.books_file)
                    return self.error_view("#The book({}) has been added to the cart of person({})#".format(b.name, p.name))

            except ValueError:
                return
    
    def get_message(self, error=""):
        return """
    {}
    {}

    BOOKS:
    {}

    {}

    Add book to one's cart: [MEN or WOMEN] person_id book_id
    ex. MEN 1 11
    ex. WOMEN 10 12
    your choose: """.format(library.men_list_string(), library.women_list_string(), library.books_list_string(), error)

class AddMan(View):
    def input_process(self, str_input):
        name = str_input
        man = Man(str_input)
        library.add_person(man)
        return self.error_view("#The man({}) has been added#".format(name))
    
    def get_message(self, error=""):
        return """
    {}
    Enter name
    ex. ali

    Enter: """.format(error) 

class AddWoman(View):
    def input_process(self, str_input):
        name = str_input
        woman = Woman(str_input)
        library.add_person(woman)
        return self.error_view("#The woman({}) has been added#".format(name))
    
    def get_message(self, error=""):
        return """
    {}
    Enter name
    ex. sarah

    Enter: """.format(error) 

class AddBookPerson(View):
    def input_process(self, str_input):
        return self

class ManageCash(View):
    def get_message(self, error=""):
        return """
    {}
    1. print factor
    2. sell books of the cart of first person and go to next person

    your choose: """.format(error)

    def input_process(self, str_input):
        if str_input == "1":
            return FactorCash()
        
        elif str_input == "2":
            return SellCash()

class FactorCash(View):
    def get_message(self, error=""):
        factor = library.get_factor()
        if factor == "":
            factor = "There isn't any person to show his/her factor"
        
        return """
    {}
    {}

    > """.format(factor, error)

class SellCash(View):
    def get_message(self, error=""):
        factor = library.sell()
        if factor == "":
            factor = "There isn't any person to show his/her factor"
        else:
            factor += "\n\tThe books has been selled"
        return """
    {}
    {}

    > """.format(factor, error)
