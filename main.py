'''Main program for calculator.
Author: Syed Saif
Created at: 21-12-2021
...
'''

import config as c
from calculation import Calculation

print(c.greeting_message)


print()

while True:
    try:
        operation_choice = int(input(
            f'''{c.operation_message} 
            {({k:v for k, v in c.operations_config.items()})}'''))

        if operation_choice == 8:
            print(c.exit_message)
            break

        result = 'No result'

        if 7 >= operation_choice >= 1:
            first_number = int(input("Enter the First Number: "))
            second_number = int(input("Enter the Second Number: "))
            calc = Calculation()
        else:
            print(f'Enter the choice between {c.operations_config.keys()}')

        if operation_choice == 1:
            result = calc.addition(first_number, second_number)

        elif operation_choice == 2:
            result = calc.subtraction(first_number, second_number)

        elif operation_choice == 3:
            result = calc.multiplication(first_number, second_number)

        elif operation_choice == 4:
            result = calc.division(first_number, second_number)

        elif operation_choice == 5:
            result = calc.modulo(first_number, second_number)

        elif operation_choice == 6:
            result = calc.exponential(first_number, second_number)

        elif operation_choice == 7:
            result = calc.floor_division(first_number, second_number)

        print(f'result = {result}')

    except ValueError as v:
        print(f'Value error due to {v}')
    except NameError as n:
        print(f'Name error due to {n}')
    except ZeroDivisionError:
        print(f'Name error due to {n}')
    except Exception as e:
        print(f'Error occured due to {e}')
