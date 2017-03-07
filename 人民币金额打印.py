a=11101
b=["零","壹","贰","叁","肆","伍","陆","柒","捌","玖"]
c=["圆","拾","佰","仟","万","拾","佰","仟"]
ans=""
if a<0:
    ans = "负"
    a = -a
for i in range(0,len(str(a))):
    if str(a)[i]!='0' or (len(str(a))-i-1 == 0 and i == 0):
        ans = ans+b[int(str(a)[i])]
        if (len(str(a))-i-1)%4!=0:
            ans = ans+c[len(str(a))-i-1]
    if (len(str(a))-i-1)%4 == 0:
            ans = ans+c[len(str(a))-i-1]
    if str(a)[i] == '0':
        if i!=len(str(a))-1:
            if str(a)[i+1] == '0':
                continue
        if (len(str(a))-i-1)%4!=0:
            ans = ans+b[0]
print(ans)
