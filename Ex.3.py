First=input("Enter the First number:")
operator=input("Enter the operator(+,-,*,/,%):")
Second=input("Enter the Second number ")
First =int(First)
Second=int(Second)
if operator=="+":
    print(First + Second)
elif operator == "-":
    print(First- Second)
elif operator =="*":
    print (First * Second)
elif operator =="/":
    print(First/Second)
elif operator =="%":
    print(First%Second)
else:
    print("INVAILD OPERATION")