import arithmetic as arith
import trigonometric as trig
from collections import OrderedDict


def menu(operations, ans=None):
    print()
    for i, operation in enumerate(operations):
        print("%i - %s" % (i+1, operation))
    print("C - Clear\nQ - Quit")
    option = input('\nChoose an operation: ')
    if option.upper() == "C":
        print("\nCleared.\n\n")
        ans = float(input('\nInsert a number: '))
        return menu(operations, ans)
    if option.upper() == "Q":
        print("Good bye!")
        return None
    option = list(operations.keys())[int(option) - 1]
    print('\n' + option.upper())
    try:
        result = operations[option](ans)
    except:
        number = float(input('\nInsert a number: '))
        try:
            result = operations[option](number)
        except:
            result = operations[option](ans, number)
    if result.is_integer():
        print('\n    RESULT:', int(result))
    else:
        print('\n    RESULT:', result)
    menu(operations, result)


if __name__ == '__main__':
    operations = OrderedDict([('Add', arith.addition),
                              ('Divide', arith.division),
                              ('Square root', arith.square_root),
                              ('nth root', arith.nth_root)])
    ans = float(input('\nInsert a number: '))
    menu(operations, ans)
