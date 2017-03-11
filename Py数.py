n = 2992
def SUM(n,m):
    sum=0
    while n>0:
        sum=sum+n%m
        n=n//m
    return(sum)
if SUM(n,10)==SUM(n,16)  and  SUM(n,10)==SUM(n,12):
    print('Yes')
else:
    print('No')