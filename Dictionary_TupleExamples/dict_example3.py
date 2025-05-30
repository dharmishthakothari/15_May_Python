student_detail = { "parth@gmail.com":["Parth",25,"Ahmedabad",34567889] ,
                  "shivani@gmail.com":["Shivani",25,"Ahmedabad",345345]}
email=input("Please Enter email ")
for k,v in student_detail.items():
    if k==email:
        for i in v:
            print(i)
print("Before Clear ",student_detail)   
student_detail.clear()
print(student_detail)   