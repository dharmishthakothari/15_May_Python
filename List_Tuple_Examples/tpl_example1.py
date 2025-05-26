tpl_number=(12,23,44,12,44,56,12)
print(tpl_number)
tpl_new_number=()
for i in tpl_number:
    print(i,tpl_number.count(i))
print("INDEX ",len(tpl_number))
for i in tpl_number:
        print(i,tpl_number.index(i))
