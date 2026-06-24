def cal():
    a=float(input("Enter first number:"))
    b=float(input("Enter second number:"))

    print("Simple Calculator")
    print("select arithmatic operations:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division") 
    choice=int(input("enter choice (1/2/3/4):"))
        
    if choice==1:
        print(f"sum of {a} and {b} is: {a+b}")
    elif choice==2:
        print(f"difference of {a} and {b} is: {a-b}")
    elif choice==3:
        print(f"product of {a} and {b} is: {a*b}")
    elif choice==4:
         print(f"division of {a} and {b} is: {a/b}")
    else:
        print("invalid choice :(")                   
cal()