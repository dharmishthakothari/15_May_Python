lst_numbers=[11,22,33,44,55,66,77,88,99]
print("Original List ",lst_numbers)
lst_numbers.insert(20,90)
print("After item added ",lst_numbers)
lst_numbers.insert(len(lst_numbers),78)
print("Item added at last ",lst_numbers)

lst_numbers[2]=9999
print("Item added at 4th position ",lst_numbers)