lst_numbers = [23,54,66,1,23,44,'wer','werwer']
sum=0
string_concate=""
for i in lst_numbers:
    if type(i)==int:
        sum+=i
    else:
        string_concate+=i
print("Numbers added ",sum)
print("String added ",string_concate)