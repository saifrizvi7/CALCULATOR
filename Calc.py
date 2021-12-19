class Calc:
    def Calculator():
            print("WELCOME TO THE SAIF'S CALCULATOR")
            Name = input("Enter your name please:")
            print("Hello " + Name + "!")
            print("Hope you will enjoy the calculation")
            print("Please choose the operations serial no. which you want to perform")
            print("1.Simple Arithmetic Operations")
            print("2.List of More operations available")   
            c=0
            option=int(input("Enter the choice which you want to perform:- "))
            def arithmetic_operation():
                def add( a, b): #Function for Addition
                    c=a+b
                    return c
        
                def sub( a, b): #Function for Subtraction
                    c=a-b
                    return c
        
                def multi( a, b):#Function for Multiplication
                    c=a*b
                    return c
        
                def divi( a, b):#Function for Division
                    c=a/b
                    return c    
                print("Here are some primary arithmetic operations like Addition, Substraction, Multiplication and Division")
                x=float(input("Enter the Value of A:- "))
                y=float(input("Enter the Value of B:- "))
                choice=int(input("Enter the Operation which you want to choose:- "))
                print("3.Addition")
                print("4.Subtraction")
                print("5.Multiplication")
                print("6.Division")
                print("7.Quit Calculator")
                result=0
                try:
                    if choice==3:
                       result=add(x,y)
                       print("The result is:-",result) 
                    elif choice==4:
                       result=sub(x,y)
                       print("The result is:-",result)             
                    elif choice==5:
                        result=multi(x,y)
                        print("The result is:-",result) 
                    elif choice==6:
                        result=divi(x,y)
                        print("The result is:-",result) 
                    elif (choice==7):
                        ch=0
                    else:
                        print("%d is not valid input. Please enter 3 ,4, 5, 6, 7." % choice)
                except ZeroDivisionError:
                        print("An error has occurred due to zero division")
                except ValueError:
                    print("%r is not valid input.  Please enter 3,4,5,6,7.",choice)
                    print("Thank you for using this calculator!") 
            def more():
                def mod( e, f): #Function for modulo
                    g=e%f
                    return g
        
                def expo( e, f): #Function for exponetial
                    g=e**f
                    return g
        
                def floor( e, f):#Function for floor division
                    g=e//f
                    return g
                print("we have more operations like Modulus,Exponentiation,Floor Division")
                u=float(input("Enter the Value of E:- "))
                v=float(input("Enter the Value of F:- "))
                print("8.Modulos Operation")
                print("9.Exponentiation")
                print("10.Floor Division")
                print("11.Quit")
                choice_m=int(input("Enter the Operation which you want to choose:- "))
                result_m=0
                try:
                    if choice_m==8:
                       result_m=mod(u,v)
                       print("The result is:-",result_m) 
                    elif choice_m==9:
                       result_m=expo(u,v)
                       print("The result is:-",result_m)             
                    elif choice_m==10:
                       result_m=floor(u,v)
                       print("The result is:-",result_m)
                    elif choice_m==11:
                       print("\nThank you for using this calculator " + Name + "!")
                    else:
                       print("%d is not valid input. Please enter 8,9,10,11." % choice_m)
                except ZeroDivisionError:
                        print("An error has occurred due to zero division")
                except ValueError:
                    print("%r is not valid input.  Please enter 8,9,10,11",choice_m)
                    print("Thank you for using this calculator!") 
            try:
                if option==1:
                    arithmetic_operation()
                elif option==2:
                    more()
                else:
                    print("%d is not valid input. Please enter 1 or 2." % option)
            except ValueError:
                print("%r is not valid input.  Please enter 1 or 2",option)
    Calculator()