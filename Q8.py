#8
num=int(input("Enter a number"))
if num%2==0:
    print("it is even")
    if num%5==0:
        print("divisible by 5")
    else:
        print("Even but not divisible by 5")
else:
    print("odd number")
