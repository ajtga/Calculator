def print_operations(operations):
    print()
    for i, operation in enumerate(operations):
        print("%i - %s" % (i+1, operation))
    print("C - Clear\nQ - Quit")


def clean_calculator(operations):
    print("\nCleared.\n\n")
    ans = float(input('\nInsert a number: '))
    return menu(operations, ans)


def quit_calculator():
    print("Good bye!")
    return None


def get_operation_by_index(operations, index):
    option = list(operations.keys())[index - 1]
    print('\n' + option.upper())
    return option


def get_result(function, a):
    try:
        return function(a)
    except:
        number = float(input('\nInsert a number: '))
        try:
            return function(number)
        except:
            return function(a, number)


def print_result(result, operations):
    if result:
        if result.is_integer():
            print('\n    RESULT:', int(result))
        else:
            print('\n    RESULT:', result)
    else:
        return clean_calculator(operations)


def menu(operations, ans=None):
    print_operations(operations)
    option = input('\nChoose an operation: ')
    if option.upper() == "C":
        return clean_calculator(operations)
    if option.upper() == "Q":
        return quit_calculator()
    chosen = operations[get_operation_by_index(operations, int(option))]
    result = get_result(chosen, ans)
    print_result(result, operations)
    menu(operations, result)
