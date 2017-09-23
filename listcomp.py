
#liscomp in python

#py 3
#nested list comp

mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9], ]

for i in range(len(mat)):
    for row in mat:
        print(row[i], end = " ")
    print()
