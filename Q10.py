#10
a=int(input("enter your 1st number which is recorded as a"))
b=int(input("enter your 2nd number which is recorded as b"))

if a>b:
    if a-b>10:
        print("a is much greater")
    else:
        print("a is slightly greater")
else:
    print("a is not greater")
