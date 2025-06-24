def authen(func):
    def wrap(*args,**kwargs):
        print(func.__name__)
        if args[0]=='admin':
            func(*args,**kwargs)        
    return wrap

@authen
def login(user):
    print(f"Welcome {user}") 

login("admin")
login("emp")
