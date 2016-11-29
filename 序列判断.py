L = [3,2,5,1,4]
L1 = sorted(L)
L2 = sorted(L, reverse=True)
if L==L1:
    print('UP')
elif L==L2:
    print('DOWN')
else:print('WRONG')