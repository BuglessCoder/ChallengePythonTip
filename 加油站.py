n=5
limit=[1,2,1,2,1]
cost=[5,1,1,1,1]
for i in range(0,n):
    sum=0
    x=i
    flag=0
    for j in range(i,i+n):
        sum=sum+limit[j%n]-cost[j%n]
        if sum<0:
            break
    if sum>=0:
        flag=1
        print(i)
if flag==0:
    print(-1)
    
        
        