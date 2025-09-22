# calcuator
m1=int(input("Enter a number") )
m2=int(input("Enter your second number") ) 
ask=input ("Enter which mathematic procedure you want to perform")
if ask=="multiply":
    x=m1*m2
    print (x)
elif ask=="divide":
    c=m1/m2
    print (c)
elif ask=="add":
    v= m1+m2
    print (v)
elif ask=="subtract":
    b=m1-m2
    print (b)
elif ask=="square":
    o=m1*m1
    p=m2*m2
    print  ("m1 square",o,"m2 square",p)  
else:
    print  ("invalid mathematic procedure") 
    
