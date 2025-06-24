#multiple
class A:
    def greet(self):
        print("Good Morning from A")
class B:
    def sayHello(self):
        print("Hello from B")
class C(A,B):
    pass
objC=C()
objC.greet()
objC.sayHello()