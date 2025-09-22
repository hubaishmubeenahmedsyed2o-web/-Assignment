#22
password="admin123"
Pass=""
while password!=Pass:
    Pass=input("Enter your correct password")
    if Pass!=password:
        print ("incorrect password")
    else:
        print("access granted")
