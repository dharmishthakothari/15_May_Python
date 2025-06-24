class PasswordVerificationError(Exception):
    # def __init__(self, msg):
    #     self.msg=msg
    #     super().__init__(msg)
    pass
def verifyPass(password):
    flag=1
    if len(password)>=8:
        for i in password:
            if ord(i)>=48 and ord(i)<=57:
                flag=1
            else:
                code=400
                msg="Password must contains digit "
                flag=0
    else:
        code=300
        msg="Password must be 8 character long digit" 
        flag=0
    if flag==0:
        raise PasswordVerificationError(msg,code)

        

password=input("Enter password ")
try:
    verifyPass(password)    
except PasswordVerificationError as e:
    print("In except block",e)
    