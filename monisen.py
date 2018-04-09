'''
Created on 2018年4月9日

@author: lidawei
'''

with open('data.txt') as fp:
    data = []
    for d in fp: 
        data.append(d)

#判断素数
def isPrime(num):
    for i in range(2,num):
        if num % i == 0 :
            return False
            break
    return True

#返回第n个素数
def prime(n):  
    if n==1:   
        return 2  
    k=1  
    i=1  
    while(k<n):  
        i+=2  
        if(isPrime(i)==True):  
            k+=1  
    return i

#返回第no个monisen数
def monisen(no):
    count=0
    i=1
    j=0
    while count<no:
        j=prime(i)
        if isPrime(2**j-1) :
            count+=1
        i+=1
    return 2**j-1
            
        