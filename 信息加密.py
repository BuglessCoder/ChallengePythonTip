a = 'abc'
b = 1
c = ''
L = list(a)
for i in range(len(L)):
    if ord(L[i])+b > ord('z'):
        c+=chr(ord(L[i])+b-26)
    else:c+=(chr(ord(L[i])+b))
print(c)