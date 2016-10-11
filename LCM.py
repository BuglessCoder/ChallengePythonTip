a = 15
b = 12
q = a
r = b
if a<b:
    t = a 
    a =b 
    b =t   
m = a%b 
while m!=0:
    a = b
    b = m
    m = a%b
        
print(q*r/b)