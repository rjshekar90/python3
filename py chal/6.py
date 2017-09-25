
"""

What the error is telling, is that you can't convert an entire list into a integer. You could get an index from the list and convert that into a integer:

x = ["0", "1", "2"]
y = int(x[0]) #accessing zeroth element
If your trying to convert a whole list into a integer, your going to have to convert the list into a string first:

x = ["0", "1", "2"]
y = str(''.join(x))# converting list into string
z = int(y)

"""


import math

c = 50
h = 30

d = input(">>> ").split(",")

#print(d)


for val in d:
    q = int(round(math.sqrt((2*c*int(d[val])/h)))
    print(q)
