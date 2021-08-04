n = int(input())
arr = list(map(int,input().split(" ")))
reversed_arr = arr[::-1]
for i in reversed_arr:
    print(i,end=' ')
