#This is the program for Calculator
class calculation:
    #This is a class for mathematical operations on numbers.
   def addition(self, a, b): #Function for Addition
      return a+b
   def subtraction(self, a, b): #Function for Subtraction
      return a-b
   def multiplication(self, a, b): #Function for Multiplication
      return a*b
   def division(self, a, b): #Function for Division
      return a/b
   def modulo(self, a, b): #Function for Modulo
      return a%b
   def exponential(self, a, b): #Function for exponential
      return a**b
   def floor_division(self, a, b): #Function for Floor Division
      return a//b
print("WELCOME TO THE SAIF'S CALCULATOR") 
name = input("Enter your nice name please: ") 
print(f"Hello {name}")
print("Hope you will enjoy the calculation")
print("Here are some basic Arithmetic Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("And some more advance operations")
print("5. Modulo")
print("6. Exponential")
print("7. Floor Division")
print("8. Exit")
while True:
   while True:
      print("Enter Your Choice from given Options(1-7): ", end="")

      try:
         operation_choice = int(input())

         if operation_choice>=1 and operation_choice<=7:
            first_number = int(input("Enter the First Number: "))
            second_number = int(input("Enter the Second Number: "))
            obj = calculation()

         if operation_choice==1:
            print(f"{first_number} + {second_number} = " + str(obj.addition(first_number, second_number)))
         elif operation_choice==2:
            print(f"{first_number} - {second_number} = " + str(obj.subtraction(first_number, second_number)))
         elif operation_choice==3:
            print(f"{first_number} * {second_number} = " + str(obj.multiplication(first_number, second_number)))
         elif operation_choice==4:
            print(f"{first_number} / {second_number} = " + str(obj.division(first_number, second_number)))
         elif operation_choice==5:
            print(f"{first_number} % {second_number} = " + str(obj.modulo(first_number, second_number)))
         elif operation_choice==6:
            print(f"{first_number} ** {second_number} = " + str(obj.exponential(first_number, second_number)))
         elif operation_choice==7:
            print(f"{first_number} // {second_number} = " + str(obj.floor_division(first_number, second_number)))
         elif operation_choice==8:
            break
         else:
            print("\nInvalid Input!..Try Again!")
         print("------------------------")

      except (ValueError, NameError, ZeroDivisionError):
         print("\n Value Error OR Name Error 0R Zero Division Error is Occured ")
         print("------------------------")
         continue

   if operation_choice==8:
       print(f"Thank you for using my calculator {name} ")
       break