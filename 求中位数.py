L = [1,2,3.5,4,5,6]
L.sort()
if len(L)%2 == 1:
    print(L[len(L)/2])
else:
    print'%.1f' % ((L[len(L)/2-1]+L[len(L)/2])/2.0)
