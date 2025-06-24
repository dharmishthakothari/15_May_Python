class NegativeValueError(Exception):
    def __init__(self, message="Value must be Postive "):
        self.message=message
        super().__init__(message)
    
try:
    print("This is my New Exception")
    val=-12
    # if val<1:
    #     raise NegativeValueError(f"Value should Positive here value is {val}")
    if val<1:
        raise NegativeValueError()
        
except NegativeValueError as e:
    print("From Exception",e)


