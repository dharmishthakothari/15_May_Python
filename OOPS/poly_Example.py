class A:
	def greet(self):
		print("Good Morning from A")
class B(A):
	
	def greet(self):
		print("Good Morning from B")
objB=B()
objB.greet()
