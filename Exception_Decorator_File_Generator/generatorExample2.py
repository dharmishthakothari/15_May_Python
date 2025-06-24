def generatorRange(start,end):
    if start>end:
        print("Not valid")
    else:
        while(start<=end):
            yield start
            start+=1
val=generatorRange(7,2)
for i in val:
    print(i)