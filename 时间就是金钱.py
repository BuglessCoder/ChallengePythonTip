st = '00:00:00'
et = '00:00:10'
'''注释内的代码不能AC，求告知why

L1=[]
L2=[]
for i in st:
    if(i!=':'):
        L1.append(int(i))
for j in et:
    if(j!=':'):
        L2.append(int(j))
    
print((L2[0]*10+L2[1]-L1[0]*10+L1[1])*3600 + (L2[2]*10+L2[3]-L1[2]*10+L1[3])*60 + (L2[4]*10+L2[5]-L1[4]*10+L1[5]))
'''


L1=list((map(int,st.split(':'))))
L2=list((map(int,et.split(':'))))
print((L2[0]-L1[0])*3600 + (L2[1]-L1[1])*60 + (L2[2]-L1[2]))
