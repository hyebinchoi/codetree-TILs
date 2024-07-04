a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

  
if a <= b and a <= c:
    print(a)
if b <= a and b <= c:
    print(b)
if c <= b and c <= a:
    print(c)