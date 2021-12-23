'''
Calculator program... Description and what this program does.

Author: Syed Saif
Created at: 21-Dec-2021
Last Modified at: 23-Dec-2021
Last Modified by: xxx
'''


class Calculation:
    '''Calculation class performs the operations like (addition, subtraction, multiplication, division, 
        modulo, exponential, floor division)
    '''

    def __init__(self):
        pass

    @staticmethod
    def addition(a, b):
        '''Performs addition of 2 numbers

        Args:
            a (numerical): first number (int or float)
            b (numerical): second number (int or float)

        Returns:
            numerical: result of addition of 2 numbers
        '''
        return a + b

    @staticmethod   
    def subtraction(a, b):
        return a - b

    '''Performs subtraction of 2 numbers

        Args:
            a (numerical): first number (int or float)
            b (numerical): second number (int or float)

        Returns:
            numerical: result of subtraction of 2 numbers
        '''
    @staticmethod
    def multiplication(a, b):
        return a * b
    
    '''Performs multiplication of 2 numbers

        Args:
            a (numerical): first number (int or float)
            b (numerical): second number (int or float)

        Returns:
            numerical: result of multiplication of 2 numbers
        '''
    @staticmethod
    def division(a, b):
        return a / b
    
    '''Performs division of 2 numbers

        Args:
            a (numerical): first number (int or float)
            b (numerical): second number (int or float)

        Returns:
            numerical: result of division of 2 numbers
        '''
    @staticmethod
    def modulo(a, b):
        return a % b
    
    '''Performs modulo of 2 numbers

        Args:
            a (numerical): first number (int or float)
            b (numerical): second number (int or float)

        Returns:
            numerical: result of modulo of 2 numbers
        '''
    @staticmethod
    def exponential(a, b):
        return a ** b
    
    '''Performs addition of 2 numbers

        Args:
            a (numerical): first number (int or float)
            b (numerical): second number (int or float)

        Returns:
            numerical: result of addition of 2 numbers
        '''
    @staticmethod
    def floor_division(a, b):
        return a // b
    
    '''Performs floor division of 2 numbers

        Args:
            a (numerical): first number (int or float)
            b (numerical): second number (int or float)

        Returns:
            numerical: result of floor division of 2 numbers
        '''
