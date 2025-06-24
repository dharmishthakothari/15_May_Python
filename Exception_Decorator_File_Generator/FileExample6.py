with open("NewFile.txt","w") as file:
    data="Hello have a nice Day!!!"
    lst_data=['This is my new String\n ','Here i am writing in File\n','End']
    file.writelines(lst_data)
    
    file.close()
