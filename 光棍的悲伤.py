a=8
sum=0
for x in bin(a).replace('0b',''):
    if x == '1':
        sum = sum+1
print(sum)
