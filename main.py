import arithmetic as arith
import trigonometric as trig
from collections import OrderedDict

operations = OrderedDict([('Add', arith.addition),
                          ('Divide', arith.division),
                          ('Square root', arith.square_root),
                          ('nth root', arith.nth_root)])



    
def menu(operations,ans=None):
    for i, operation in enumerate(operations):
        print("%i - %s" % (i+1, operation))
    option = int(input('\nChoose an operation: ')) - 1
    option = list(operations.keys())[option]
    print('\n' + option.upper())
    try:
        result = operations[option](ans)
    except:
        number = int(input('\nInsert a number: '))
        try:
            result = operations[option](number)
        except:
            result = operations[option](ans,number)
    print('\nResult:', result)
    menu(operations,result)

if __name__ == '__main__':
    ans = int(input('\nInsert a number: '))
    menu(operations,ans)
