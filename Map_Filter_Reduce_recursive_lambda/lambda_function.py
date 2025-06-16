def findmax(number1,number2):
    if number1>number2:
        return number1
    else:
        return number2
max_number=findmax(120,22)
print(max_number)
max_number=lambda number1,numbers2:number1 if number1>numbers2 else numbers2
print(max_number(120,2289))