def addition(a, b):
    """Returns the sum of the numbers a and b"""
    return a+b

def subtraction(a, b):
    """Returns the subtraction of the numbers a and b"""
    return a-b

def multiplication(a, b):
    """Returns the multiplication of the numbers a and b"""
    return a*b

def division(a, b):
    """Returns the division of the number a by the number b"""
    if b == 0:
        return("Error! Division by 0")
    else:
        return a/b

def nth_root(a, b):
    """Returns the "bth" root of the number a"""
    return a**(1/b)

def square_root(a):
    """Returns the square root of the number a"""
    return nth_root(a, 2)

def cubic_rooth(a):
    """Returns the cubic root of the number a"""
    return nth_root(a, 3)

def exponentiation(a, b):
    """Returns the exponentiation of the number a by the number b"""
    return a**b
