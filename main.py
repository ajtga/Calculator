import Math.arithmetic as arith
import Math.trigonometric as trig
from collections import OrderedDict
from gui.interface import menu


operations = OrderedDict([('Add', arith.addition),
                          ('Subtract', arith.subtraction),
                          ('Multiply', arith.multiplication),
                          ('Divide', arith.division),
                          ('Square root', arith.square_root),
                          ('Cubic root', arith.cubic_root),
                          ('nth root', arith.nth_root),
                          ('nth power', arith.exponentiation),
                          ('Sine (Radians)', trig.sine),
                          ('Cosine (Radians)', trig.cosine),
                          ('Tangent (Radians)', trig.tangent),
                          ('Arcsine (Radians)', trig.arcsine),
                          ('Arccosine (Radians)', trig.arccosine),
                          ('Arctangent (Radians)', trig.arctangent),
                          ('Cosecant (Radians)', trig.cosecant),
                          ('Secant (Radians)', trig.secant),
                          ('Cotangent (Radians)', trig.cotangent)])
ans = float(input('\nInsert a number: '))
menu(operations, ans)
