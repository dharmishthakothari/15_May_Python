lst_numbers=[1,2,3,4,5,6]
lst_new_list=[]
count=0
# for i in lst_numbers:
#     lst_new_list.insert(count,i*i*i)
#     count+=1
lst_new_list=[i*i for i in lst_numbers]
print(lst_new_list)