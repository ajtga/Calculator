import math


def sine(x):
    return math.sin(x)


def cosine(x):
    return math.cos(x)


def tangent(x):
    return math.tan(x)


def arcsine(x):
    return math.asin(x)


def arccosine(x):
    return math.acos(x)


def arctangent(x):
    return math.atan(x)


def cosecant(x):
    try:
        return 1/math.sin(x)
    except ZeroDivisionError:
        print('\nERROR! Division by zero.')
        return False
