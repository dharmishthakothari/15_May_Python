#Multilevel
class A:
    def greet(self):
        print("Good Morning...")
class B(A):
    pass
class C(B):
    pass
objC=C()
objC.greet()
objB=B()
objB.greet()