import sys
s = input()
try:
    to_int=int(s)
    print(to_int)
except ValueError:
    print('Bad String')
