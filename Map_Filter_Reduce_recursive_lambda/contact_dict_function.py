contacts={}
# Add Contact name-number
# View All Contact
# Search Contact
# Delete Contact
# Exit 

def addContact(dicContacts,name,number):
    dicContacts[name]=number
    return dicContacts
def viewAllContact(dictContact):
    for k,v in dictContact.items():
        print(k,'--->',v)
def searchContact(dictContacts,name):
    for k,v in dictContact.items():
        if k==name:
            return v
    else:
        return f"{name} not found in {dictContact.keys()}"
        
    
def deleteContact(dictContacts,name):
    for k,v in dictContacts.items():
        if k==name:
            del dictContacts[name]
            return f"{name} deleted from contacts {dictContact.keys()}"
    else:
        return f"{name} not found in {dictContact.keys()}"

status=True
while status:
    print("1.Add Contact")
    print("2.Search Contact")
    print("3.ViewAll Contact")
    print("4.Delete Contact")
    print("5. Exit")

    val=int(input("Please Enter your choice : "))
    match val:
        case 1:
            name,contact=input("Please enter name and contact").split()
            dictContact=addContact(contacts,name,contact)
        case 2:  
            name=input("Please Enter name ")
            print(searchContact(dictContact,name))
        case 3:
            viewAllContact(dictContact)
        case 4:
            name=input("Please Enter name ")
            print(deleteContact(dictContact,name))
            viewAllContact(dictContact)
        case 5:break
        case _:print("Please Enter your choice ")
            
