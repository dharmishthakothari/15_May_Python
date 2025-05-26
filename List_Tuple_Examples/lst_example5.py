lst_city=['Ahemdabad','baroda','surat','Rajkot']
for i in lst_city:
    i=i.capitalize()
    print(i)

for i in range(len(lst_city)):
    lst_city[i]=lst_city[i].capitalize()

print("City List ",lst_city)