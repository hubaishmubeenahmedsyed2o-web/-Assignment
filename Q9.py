#9
username=input("enter your username")
password=input("enter your password")

if username=="admin":
    if password=="1234":
        role=input("enter your role")
        if role=="manager":
            print("Welcome manager")
        else:
            print("access granted")
    else:
        print("wrong password")
else:
    print("invalid username")
