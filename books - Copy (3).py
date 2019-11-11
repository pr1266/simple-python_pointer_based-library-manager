class Book:

    def __init__(self , name , publish_year , price):
        self.name = name
        self.publish_year = publish_year
        self.price = price
        
    def __str__(self):
        return "{} {} {}".format(self.name, self.publish_year, self.price)

    __repr__ = __str__
    
class Books:
    
    def __init__(self):
        self.__list = []
        self.__i = -1
    
    def len(self):
        return len(self.__list)

    def add(self , book):
        self.__list.append(book)
    
    def erase(self, name):
        it = iter(self)
        for i in range(self.len()):
            it = next(it)
            if it.name == name:
                del self.__list[i]
                return
    
    def save(self):
        with open("book-list.txt", "a+") as file:
            it = iter(self)
            for i in range(self.len()):
                it = next(it)
                file.write(str(it) + "\n")
                
    def __iter__(self):
        return self

    def __next__(self):
        self.__i += 1
        if self.__i == len(self.__list):
            self.__i = 0
        return self.__list[self.__i]
