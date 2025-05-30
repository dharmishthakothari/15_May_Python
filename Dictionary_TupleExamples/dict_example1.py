dict_first={1:"One" , 2:"Two" , 3:"Three" , 4:"Four",2:"Thwenty Two",5:"Four"}
print(dict_first)
print(type(dict_first.keys()))
print(type(dict_first.values()))
for i in dict_first.keys():
    print(i)
for i in dict_first.values():
    print(i)
print(dict_first.items())
for k,v in dict_first.items():
    print(k,v)
for i in dict_first.items():
    print(i)