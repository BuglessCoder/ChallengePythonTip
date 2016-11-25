a = 3
b = 60
for i in range(a,b):
    for j in range(a,b):
        x = i
        y = j
        if(y<x):
            t = y
            y = x
            x = t
        m = y%x
        while(m!=0):
            y = x
            x = m;
            m = y%x;
        if x == a and i*j/x == b:
            if i<j:
                print(i,j)