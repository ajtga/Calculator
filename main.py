import arithmetic as arith
import trigonometric as trig
from collections import OrderedDict


def print_operations():
    print()
    for i, operation in enumerate(operations):
        print("%i - %s" % (i+1, operation))
    print("C - Clear\nQ - Quit")
    
    
def clean_calculator():
    print("\nCleared.\n\n")
    ans = float(input('\nInsert a number: '))
    return menu(operations, ans)


def quit_calculator():
    print("Good bye!")
    return None


def get_operation_by_index(index):
    option = list(operations.keys())[index - 1]
    print('\n' + option.upper())
    return option
    

def get_result(chosen, a):
    try:
        return operations[chosen](a)
    except:
        number = float(input('\nInsert a number: '))
        try:
            return operations[chosen](number)
        except:
            return operations[chosen](a, number)

    
def print_result(result):
    if result.is_integer():
        print('\n    RESULT:', int(result))
    else:
        print('\n    RESULT:', result)
        
        
def menu(operations, ans=None):
    print_operations()
    option = input('\nChoose an operation: ')
    if option.upper() == "C":
        return clean_calculator()
    if option.upper() == "Q":
        return quit_calculator()
    chosen = get_operation_by_index(int(option))
    result = get_result(chosen, ans)
    print_result(result)
    menu(operations, result)


if __name__ == '__main__':
    operations = OrderedDict([('Add', arith.addition),
                              ('Divide', arith.division),
                              ('Square root', arith.square_root),
                              ('nth root', arith.nth_root)])
    ans = float(input('\nInsert a number: '))
    menu(operations, ans)
