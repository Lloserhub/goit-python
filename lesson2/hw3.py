number, oper = None, None
final_value = 0.0

while oper == None:
    while number == None:
        try:
            number = float(input('Please enter a number: '))
        except ValueError:
            print('Incorrect value. Please, try again.')
            number = None

    while oper == None:
            oper = input('Enter oper: ')
            if oper not in ('/', '*', '-', '+', '='):
                print('Incorrect value. Please, try again.')
                oper = None

    if oper == '/':
        final_value = final_value/number
        number = None
        oper = None
        print(f'Final Value: {final_value}')

    if oper == '*':
        final_value = final_value*number
        number = None
        oper = None
        print(f'Final Value: {final_value}')

    if oper == '-':
        final_value = final_value-number
        number = None
        oper = None
        print(f'Final Value: {final_value}')

    if oper == '+':
        final_value = final_value+number
        number = None
        oper = None
        print(f'Final Value: {final_value}')

    if oper == '=':
        print(f'Final Value: {final_value}')

    