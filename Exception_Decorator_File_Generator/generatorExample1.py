def simple_generator():
    
    yield 22
    yield 1
    yield 16
    yield 15
    yield "11"


val=simple_generator()
print(val,type(val))
for i in val:
    print(type(i))
