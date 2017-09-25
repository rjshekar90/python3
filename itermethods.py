

# __iter__() and __next__()

class Reverse:
    """ Iterator for looping over a seq backwards """

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

for char in Reverse("Spam"):
    print(char)
