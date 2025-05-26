lst_numbers = [23,34,12,45,67,88]
lst_even_numbers=[]
# for i in lst_numbers:
#     if i%2==0:
#         lst_even_numbers.append(i)

lst_even_numbers =[i for i in lst_numbers if i%2==0]
print(lst_even_numbers)
