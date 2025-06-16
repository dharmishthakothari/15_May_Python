list_number=[1,2,3,4]
list_number2=[140,13,124,1231]
def add(x,y):
    return x+y
add_2_nu=lambda x,y:x+y
j=0
list_new=[]
for i in list_number:
    list_new.append(add_2_nu(i,list_number2[j]))
    j+=1
print(list_new)
new_list=list(map(add,list_number,list_number2))
print(new_list)