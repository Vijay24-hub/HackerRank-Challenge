n = int(input())
new_dict = {}
for i in range(n):
    x = input().split()
    new_dict[x[0]] = x[1]
while True:
    try:
        name = input()
        if name in new_dict:
            print(f"{name}={new_dict[name]}")
        else:
            print("Not found")
    except:
        break
