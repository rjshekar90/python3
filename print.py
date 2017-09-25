
#pretty print

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

for name, phone in table.items():
    print("{0:9} ==> {0:10}".format(name, phone))
