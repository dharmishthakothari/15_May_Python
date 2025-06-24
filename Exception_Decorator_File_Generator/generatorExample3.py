sq=[i*i for i in [23,45,67]]
print(sq)

sq1=(i*i for i in [23,45,67])
print(sq1)

#for i in sq1:
print(next(sq1))
print(next(sq1))
print(next(sq1))







sq2={i for i in [23,45,67]}
print(sq2)