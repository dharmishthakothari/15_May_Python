import json
with open("MyJsonFile.json","w") as file:

    data = {'name':'Suraj','age':20,'name':'Deep'}
#file = open("MyJsonFile.json","w")
    json.dump(data,file)

    print("Data Written Successfully ")

    # data1=json.load(file)
    
    # print(data1['name'])

