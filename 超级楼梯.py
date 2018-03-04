n=5
def fei(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fei(n-1) + fei(n-2)
    else:
        return 0
print(fei(n))
