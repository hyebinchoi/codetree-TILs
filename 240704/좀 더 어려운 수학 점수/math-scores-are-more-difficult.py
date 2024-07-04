a,b = input().split()
c,d = input().split()

a = int(a) 
b = int(b)
c = int(c)
d = int(d)

if a>c or (a == c) and (b > d) :
    print("A")
elif c>a or (a == c) and (d > b) :
    print("B")