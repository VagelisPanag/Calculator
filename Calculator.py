class MyCalculator:

    def add_numbers(x,y):
        result = x + y
        print(f'Adding -> {x:g} + {y:g} = {result:g}')

    def subtract_numbers(x,y):
        result = x - y
        print(f'Subtracting -> {x:g} - {y:g} = {result:g}')

    def multiply_numbers(x,y):
        result = x * y
        print(f'Multiplying -> {x:g} * {y:g} = {result:g}')
    
    def divide_numbers(x,y):
        result = x / y
        print(f'Dividing -> {x:g} / {y:g} = {result:g}')
    
    def modulo_numbers(x,y):
        result = x % y
        print(f'Doing modulo -> {x:g} mod {y:g} = {result:g}')

    def raise_number(x,y):
        result = x ** y
        print(f'Raising {x:g} to the power of {y:g} = {result:g}')


def get_parameters():
    while True:
        try:
            user_input1 = input('Please enter the first number (integer/decimal): ')
            x = float(user_input1)
            break
        except:
            print('Enter a valid number!')

    while True:
        all_operands = ['+','-','*','/','%','**']
        operand = input('Please press "+" to add, "-" to subtract, "*" to multiply, "/" to divide, "%" to modulo or "**" to raise to a power: ')
        if operand in all_operands:
            break
        else:
            print('Please enter a valid operand!')

    while True:
        try:
            if operand == '**':
                user_input2 = input(f'To which power you want to raise {x:g} ? :')
            else:
                user_input2 =  input('Please enter the second number (integer/decimal): ')
            y = float(user_input2)
            if operand == '/' and y == 0:
                print('Cannot divide by zero(0), please give a new value!')
            else:
                break
        except:
            print('Enter a valid number!')
    return x,operand,y

def operand_decision(values):
    x,operand,y = values
    if operand == '+':
        MyCalculator.add_numbers(x,y)
    elif operand == '-':
        MyCalculator.subtract_numbers(x,y)
    elif operand == '*':
        MyCalculator.multiply_numbers(x,y)
    elif operand == '/':
        MyCalculator.divide_numbers(x,y)
    elif operand == '%':
        MyCalculator.modulo_numbers(x,y)
    elif operand == '**':
        MyCalculator.raise_number(x,y)
    else:
        print('Uknown error!')

def main():
    # values = get_parameters()
    # operand_decision(values)
    loop = 1
    times_used = 1
    while True:
        if loop == 1:
            operand_decision(get_parameters())
            loop += loop
        else:
            cont = input('If you want to continue press "y" else press "n": ')
            if cont.lower() == 'y':
                times_used += times_used
                operand_decision(get_parameters())
            elif cont.lower() == 'n':
                print ('You used the calculator ' + str(times_used) + ' times!')
                print('Thank you!')
                break
            else:
                print('Invalid input! Please try again!')

if __name__ == '__main__':
    # print('Running from main program!')
    main()