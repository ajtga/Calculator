from math import sin, cos, tan, asin, acos, atan


def sine(x):
    return sin(x)


def cosine(x):
    return cos(x)


def tangent(x):
    return tan(x)


def arcsine(x):
    return asin(x)


def arccosine(x):
    return acos(x)


def arctangent(x):
    return atan(x)


def cosecant(x):
    try:
        return 1/sin(x)
    except ZeroDivisionError:
        print('\nERROR! Division by zero.')
        return False


def secant(x):
    try:
        return 1/cos(x)
    except ZeroDivisionError:
        print('\nERROR! Division by zero.')
        return False


def cotangent(x):
    try:
        return 1/tan(x)
    except ZeroDivisionError:
        print('\nERROR! Division by zero.')
        return False
