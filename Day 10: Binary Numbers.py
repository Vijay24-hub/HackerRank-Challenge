num=int(input())
res=0
flag=0
while num>0:
    if num%2==1:
        res+=1
        if res>flag:
            flag=res
    else:
        res=0
    num//=2
print(flag)
