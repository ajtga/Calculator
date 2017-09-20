def addition(a,b):
    return a+b

def multiplication(a, b):
    return a*b
    
def division(a,b):
    if b==0:
        return("Error! Division by 0")
    else:
        return a/b

def nth_root(a,b):
    return (a**(1/b))

def square_root(a):
    return nth_root(a,2)

def cubic_rooth(a):
    return nth_root(a, 3)