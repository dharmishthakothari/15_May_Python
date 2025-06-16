lst_numbers=[1,2,3,4,6,7,8]
def findEven(ele):
    if ele%2!=0:
        return ele

even_list=filter(findEven,lst_numbers)
print(list(even_list))
