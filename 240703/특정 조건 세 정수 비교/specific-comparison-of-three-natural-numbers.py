a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a <= b and a <= c :
    print(1, end=" ")
else :
    print(0, end=" ")
if a == b and b == c :
    print(1)
else : 
    print(0)