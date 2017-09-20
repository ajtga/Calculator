import arithmetic as arith
import trigonometric as trig
from collections import OrderedDict
from interface import menu




if __name__ == '__main__':
    operations = OrderedDict([('Add', arith.addition),
                              ('Divide', arith.division),
                              ('Square root', arith.square_root),
                              ('nth root', arith.nth_root)])
    ans = float(input('\nInsert a number: '))
    menu(operations, ans)
