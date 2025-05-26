lst_numbers = [12,34,67,45,22,65]
lst_even_numbers=[34,56,78,90]
for i in lst_numbers:
    if i%2==0:
        print(i)
lst_whole = lst_numbers+lst_even_numbers
print(lst_whole)