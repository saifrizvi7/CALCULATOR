'''
Calculator program... Description and what this program does.

Author: Syed
Created at: 21-Dec-2021
Last Modified at: xx-Dec-2021
Last Modified by: xxx
'''


class Calculation:
    '''Calculation class performs the operations like (addition, subtraction...)
    '''

    def __init__(self):
        pass

   #! If you dont use self, you can create it as static method

    @staticmethod
    def addition(a, b):
        '''Performs addition of 2 numbers

        Args:
            a (numerical): first number (int or float)
            b (numerical): second number (int or float)

        Returns:
            numerical: result of addition of 2 numbers
        '''
        return a+b

    @staticmethod
    def subtraction(a, b):
        return a-b
