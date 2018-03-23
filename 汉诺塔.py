#汉诺塔移动过程输出（a b c代表三个针，目标是要从a借助b移到c）：
def hanoi(a,b,c,n):
    if n == 1:
        print(a+'->'+c)
        
    else:
        hanoi(a, c, b, n-1)
        print(a+'->'+c)
        hanoi(b, a, c, n-1)
    
n = 4
hanoi('a', 'b', 'c', n)

#汉诺塔最少步数：f(n) = 2f(n-1)+1，移动累加消项最后等号右边得到一个等比数列的和，最后结果f(n)=2^n-1
print('最少步数：' + str(2**n-1))