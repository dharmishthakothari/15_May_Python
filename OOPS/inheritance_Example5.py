class A:
    def greet(self):
        print("Good Morning from A")
class B(A):
    pass
class C(A):
    pass
objB=B()
objB.greet()
objC=C()
objC.greet()
