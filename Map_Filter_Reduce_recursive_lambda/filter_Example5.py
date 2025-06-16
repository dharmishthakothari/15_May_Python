lst_city = ["Ahmedabad","Baroda","Surat","Rajkot",'ttt']

def findA(name):
    #if name[0] in "aeiou":
    
    val=name.count('o')
    if val>=0:
        return val
    

l2 = list(filter(findA,lst_city))
print(l2)