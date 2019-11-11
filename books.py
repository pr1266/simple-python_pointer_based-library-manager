class Book:

    def __init__(self , name , publish_year , price):
        self.name = name
        self.publish_year = publish_year
        self.price = price
        
    def __str__(self):
        return "{} {} {}".format(self.name, self.publish_year, self.price)

    __repr__ = __str__
    
    
class BookNode:
    
    def __init__(self , book, next_node=None):
        self.next_node = next_node
        self.book = book

    def __str__(self):
        return str(self.book)

    __repr__ = __str__

class BooksHead:
    
    def __init__(self , book=None):
        
        self.first = None
        self.last = None
        self.count = 0

        if book is not None:
            self.add(book)
    
    def add(self , book):
        if self.count == 0:
            new_node = BookNode(book)
            new_node.next_node = new_node
            self.first = new_node
            self.last = new_node
        else:
            new_node = BookNode(book)
            self.last.next_node = new_node
            new_node.next_node = self.first
            self.last = new_node
        self.count += 1
    
    def save(self, file_name):
        with open("book-list.txt", "w+") as file:
            for books in self:
                file.write(str(books) + "\n")

    def __getitem__(self, key):
        j = 0
        for i in self:
            if j == key:
                return i
            j += 1
        return None

    def __delitem__(self, key):
        j = 0
        before = self.last

        if key == 0:
            if self.count == 0:
                raise IndexError()
            if self.count == 1:
                del self.first
                self.first = None
                self.last = None
            else:
                tmp = self.first
                self.first = self.first.next_node
                del tmp
            self.count -= 1
            return
        for i in self:
            if j == key:
                before.next_node = i.next_node
                del i
                self.count -= 1
                return
            j += 1
            before = i
        raise IndexError()

    def __iter__(self):
        return BooksIterator(self)

class BooksIterator():
    def __init__(self, books_head):
        self.books_head = books_head
        self.book_node = books_head.first
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        x = self.book_node
        if x!= None and x.next_node == None or self.i >= self.books_head.count:
            raise StopIteration()
        self.i += 1
        self.book_node = x.next_node
        return x