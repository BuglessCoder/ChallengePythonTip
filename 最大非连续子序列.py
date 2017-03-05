L = [2,-3,3,50]
if len(L)<=2:
    print(max(L))
tm = max(L[0],0)
for i in range(2,len(L)):
    L[i]+=tm
    tm = max(tm,L[i-1])
print(max(L))