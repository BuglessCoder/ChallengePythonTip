L = [2]
for x in range(3,100):
    a = 0
    for y in range(2,x):
        if(x % y == 0):
            a = 1
    if(a == 0):   
        L.append(x)
print(' '.join(map(str,L)))