
# fact

def fact(x):
    if x == 0:
        return 1
    else:
        return fact(x-1) * x

print(fact(5))
