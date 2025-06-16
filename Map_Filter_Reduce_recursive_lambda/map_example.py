def square(no):
    return no*no
list_numbers=[1,2,3,4,5,7,8,9,10]
list_numbers_square=[]
# for i in list_numbers:
#     list_numbers_square.append(square(i))
list_numbers_square=list(map(square,list_numbers))
print(list_numbers_square)


