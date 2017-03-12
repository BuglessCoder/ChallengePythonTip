n=2
def sushu(a):
    for i in range(2,a):
        if a%i==0:
            return False;
            break;
        return True;
count=0    
for i in range(2,n//2):
    if(sushu(i) and sushu(n-i)):
                count+=1;
                    
print(count)              
      
    