a = 12
b = 16
n = 0
if a<b:
    t = a
    a = b
    b =t
for x in range(1,a):
    if a%x==0 and b%x==0:
        n = n+1
print(n)
