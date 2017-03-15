n=3
pre=1
now=0
for i in range(0,n):
    pre,now=now,pre+now
print(now%20132013)
