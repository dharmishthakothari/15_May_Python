import time,datetime
def deco(funcname):
    def wrap():
        print("Before Execution ",datetime.datetime.now())        
        funcname()
        print("After Execution ",datetime.datetime.now())
    return wrap

@deco
def getmsg():
    print("Good Morning!!!")

@deco
def add():
     for i in range(100):
        print(i)

getmsg()
add()
