L=[2,8,3,50]
a=b=0
for i in range(len(L)):
    while L[i]%2==0:
		a=a+1
		L[i]/=2
    while L[i]%5==0:
		b=b+1
		L[i]/=5
print min(a,b) 