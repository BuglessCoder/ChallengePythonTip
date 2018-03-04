n=10
def isPrime(a):
    flag = 0
    for i in range(2,a):
        if a%i==0:
            flag = 1
            break;
    if flag == 1:
        return False
    else:
        return True
count=0    
for i in range(2,n//2+1):
    if(isPrime(i) and isPrime(n-i) and i!=n-i):
                count+=1;       
print(count)              
      
    