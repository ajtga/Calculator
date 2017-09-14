import arithmetic as arith
import trigonometric as trig
from collections import OrderedDict

operations = OrderedDict([('Add', arith.addition),
                          ('Divide', arith.division),
                          ('Square root', arith.square_root),
                          ('nth root', arith.nth_root)])

def menu(operations):
    for i, operation in enumerate(operations):
        print("%i - %s" % (i+1, operation))
    option = int(input('\nChoose an operation: ')) - 1
    option = list(operations.keys())[option]
    print('\n' + option.upper())
    print('\nResult:', operations[option]())

if __name__ == '__main__':
    menu(operations)
