a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if (a > b and a < c) or (a > c and a < b):
    print(a)
elif (b > a and b < c) or (b > c and b < a):
    print(b)
else:
    print(c)