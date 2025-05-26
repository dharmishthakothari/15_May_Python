lst_numbers = [23,34,12,45,67,88]
lst_even_numbers=[]
# for i in lst_numbers:
#     if i%2==0:
#         lst_even_numbers.append('EVEN')
#     else:
#         lst_even_numbers.append('ODD')

lst_even_numbers =['EVEN'  if i%2==0 else 'ODD' for i in lst_numbers]
print(lst_even_numbers)
