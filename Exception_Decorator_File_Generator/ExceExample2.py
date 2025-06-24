try:
    number1=int(input("Please enter number "))
    number2=int(input("Please enter number2 "))
    ans=number1+number2
    print(ans)
    ans=number1/number2
    print(ans)
except ValueError:
    print("In ValueError")
except ZeroDivisionError:
    print("In DivisionError")

