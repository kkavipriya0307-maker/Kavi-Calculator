try:
    tit = " Welcome to Kavi Calculator "
    print("="*40)
    print("{0:^40s}".format(tit))
    print("="*40)
    
    hist = []
    def calculator():
        print("Enter 2 Numbers To do operations!")
        n1 = int(input("Enter Number 1: "))
        n2 = int(input("Enter Number 2: "))
        option ='''
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division '''
        print("{0:^40s}".format(option))
        o = input("Enter Option(1/2/3/4): ")
         
        if (o == '1'):
            t = n1 + n2
            print(f"Sum = {t}")
        elif (o == '2'):
            t = n1 - n2
            print(f"Difference = {t}")
        elif(o == '3'):
            t = n1 * n2
            print(f"Multiply = {t}")
        elif (o == '4'):
            t = n1 / n2
            print(f"Divide = {t}")
        else:
            print("Invalid Option")

        if(o == '1'):
            o = '+'
        elif(o == '2'):
            o = '-'
        elif(o == '3'):
            o = '*'
        else:
            o = '/'

        history = f"{n1} {o} {n2} = {t}"
        hist.append(history)

        n = input("Enter If you want to see the History(y/n): ")
        if (n == 'y'):
            print("Calculation History!")
            for i in hist:
                print(i)
        else:
            print("Continue your Calculation")

    calculator()
    
    while True:

        lop = input("Do you want to repeat the operations(y/n): ")
        
        if(lop == 'Y' or lop == 'y'):
            calculator()
        
        elif(lop == 'N' or lop == 'n'):
            print("Loop is Stopped")
            break

        else:
            print("Invalid!")
            break

except ZeroDivisionError:
    print("Cannot divide by zero!")

finally:
    mess = """Your Operation has been Done Well!!
        Thank you for using Kavi Calculator!
        Have a nice day!"""
    print("{0:^40}".format(mess))
