dict_number = {1:11,2:22,3:33,4:44}
dict_another_number = dict_number
print(dict_number)
print(dict_another_number)
dict_number[2]=89
print(dict_number)
print(dict_another_number)
dict_number.clear()
print(dict_number)
print(dict_another_number)

