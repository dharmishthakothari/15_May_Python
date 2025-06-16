def fact(number):
    if number==0 or number==1:
        return 1
    else:
        print(number)
        return number*fact(number-1)
print(fact(5))