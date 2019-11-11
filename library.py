import os.path

from persons import *
from books import *


class Library:
    
    def __init__(self, books_file):
        self.books = BooksHead()
        self.books_file = books_file

        with open(books_file, "r") as file:
            line = file.readline()
            while line:
                data = line.split(' ')
                b = Book(data[0], int(data[1]), int(data[2]))
                self.books.add(b)
                line = file.readline()

        self.men_turn = True
        self.women_queue = []
        self.men_queue = []
        self.money = 0
        
    def books_list_string(self):
        string = ""
        j = 0
        for i in self.books:
            j += 1
            string += "\t {}. {}\n".format(j, str(i))
        return string

    def men_list_string(self):
        string = "MEN: \n"
        j = 0
        for i in self.men_queue:
            j += 1
            string += "\t {}. {}\n".format(j, str(i.name))
        return string
    
    def women_list_string(self):
        string = "WOMEN: \n"
        j = 0
        for i in self.women_queue:
            j += 1
            string += "\t {}. {}\n".format(j, str(i.name))
        return string


    def add_book(self, book):
        self.books.add(book)
        self.books.save(self.books_file)

    def add_person(self, person):
        if type(person) == Woman:
            self.women_queue.append(person)
        else:
            self.men_queue.append(person)
            
    def get_person(self):
        ret = None
        if self.men_turn and len(self.men_queue) != 0:
            ret = self.men_queue[0]
        elif len(self.women_queue) != 0:
            ret = self.women_queue[0]
        if ret == None and len(self.men_queue) != 0:
            ret = self.men_queue[0]
        return ret

    def pop_person(self):
        ret = None
        ret = self.get_person()
        if type(ret) == Man:
            self.men_turn = False
            del self.men_queue[0]
        elif type(ret) == Woman:
            self.men_turn = True
            del self.women_queue[0]
        return ret
    
    def get_factor(self):
        person = self.get_person()
        if person == None:
            return ""
        string = ""
        total_price = 0
        i = 0
        string += "This is the cart of {} in {}\n\t".format(person.name, "Men" if type(person) == Man else "Women" )
        string += "index - name - publish year - price\n"
        for book in person.cart:
            i += 1
            string += "\t" + str(i) + " " + str(book) + "\n"
            total_price += book.price

        string += "\ttotal price: " + str(total_price) + "\n"
        return string
    
    def sell(self):
        factor = self.get_factor()
        person = self.pop_person()
        return factor

library = Library("book-list.txt")