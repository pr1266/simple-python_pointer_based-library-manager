class Test:
    def __init__(self):
        self.i = 0

    def add(self, value):
        self.l.append(value)

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i == 20:
            raise StopIteration()
        return self