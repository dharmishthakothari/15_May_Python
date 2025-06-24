file=open("NewFile.txt","w")
data="Hello have a nice Day!!!"

len_str=file.write(data)
if len(data)==len_str:
    print("Data Written successfully...")