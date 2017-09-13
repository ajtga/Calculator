def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b==0:
        return("Error! Division by 0")
    else:
        return a/b
    
def square_root(a):
    return (a**(1/2))

def nth_root(a,b):
    return (a**(1/b))

def cube_root(a):
    return (a**(1/3))

def exponentiation(a,b):
    return a**b
