list_mix=[1,2,23.54,'test',23.45,78,56]
# def findInt(ele):
#     if isinstance(ele,int):
#         return ele
# for i in list_mix:
#     print(findInt(i))
lst_int=list(filter(lambda ele: isinstance(ele,int),list_mix))
print(lst_int)
