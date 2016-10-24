L=[2,8,3,50]
def cheng(a,b):
    return a*b;
def is0(n):
    return n != '0'
L1 = list(filter(is0,list(str(reduce(cheng, L)))))
if int(L1[-1])%2 == 0:
    print(0)
else: print(1)
