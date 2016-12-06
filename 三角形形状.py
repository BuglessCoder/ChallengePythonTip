a=3
b=4
c=5
a,b,c = sorted([a,b,c])
if (a+b)>c:
    if a*a+b*b>c*c:
        print("R")
    elif a*a+b*b<c*c:
        print("D")
    elif a*a+b*b==c*c:
        print("Z")    
else:print("W")
