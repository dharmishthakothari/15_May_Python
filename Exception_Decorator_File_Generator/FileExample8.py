import json
no_of_data =int(input("Please Enter no.of Items you want to add in file..."))
data={}
for i in range(0,no_of_data):
    product=input("Please enter product ")
    name = input(f"Please enter name of {product}  ")
    price=int(input("Please enter price "))
    data[product]={'name':name,'Price':price}
    
print(data)
with open("MyProductFile.json","w") as file:
    json.dump(data,file)
    print("Data Written Successfully ")
