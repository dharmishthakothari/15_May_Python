class Phone:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price
class PhoneInventary:
    def __init__(self,lstPhone):
        self.lstPhone=lstPhone
    def addPhone(self,phone):
        self.lstPhone.append(phone)
    def viewPhones(self):
        return self.lstPhone
mi=Phone("MI","Note13",23456)
s1=Phone("Samsung","Galaxy",45678)
lstPhone=[]
invetary=PhoneInventary(lstPhone)
invetary.addPhone(mi)
ansList=invetary.viewPhones()
for i in ansList:
    print(i.name,i.model,i.price)
        