import arithmetic as arith
import trigonometric as trig
from collections import OrderedDict
from interface import menu


operations = OrderedDict([('Add', arith.addition),
                          ('Subtract', arith.subtraction),
                          ('Multiply', arith.multiplication),
                          ('Divide', arith.division),
                          ('Square root', arith.square_root),
                          ('Cubic root', arith.cubic_root),
                          ('nth root', arith.nth_root),
                          ('nth power', arith.exponentiation)])
ans = float(input('\nInsert a number: '))
menu(operations, ans)
