'''
Created on 2018年4月9日

@author: lidawei
'''
def countchar(str):
    charDict={}
    for i in range(26):
        charDict[chr(i+65)]=0
    str=str.upper()
    for x in str:
        if ord('A')<=ord(x)<=ord('Z'):
            charDict[x]+=1
        else:
            continue
    return [charDict[chr(i+65)] for i in range(26)]    

if __name__ == "__main__":
        print(countchar(input()))
            