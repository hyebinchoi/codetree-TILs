a,b,c = input().split()


a = int(a)
b = int(b)
c = int(c)


if a > b and b > c :
    print(b)
if (a > b and c > b) and a > c :
    print(c)

if b > a and a > c :
    print(a)
if (b > a and c > a) and a > b :
    print(b)

if c > a and a > b :
    print(a)
if (c > a and b > a) and b > c :
    print(c)