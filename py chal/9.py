

#caps


list = []
while True:
    n = input(">>> ")
    if n:
        list.append(n.upper())
    else:
        break

for char in list:
    print("".join(char), end = " ")    
