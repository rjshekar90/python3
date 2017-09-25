

#generators.py
#comes with built in __iter__() and __next__() and
#raises Stopiteration method automatically

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse("hello"):
    print(char)



#generators expr.
"""
sum(i*i for i in range(10))                 # sum of squares

"""
