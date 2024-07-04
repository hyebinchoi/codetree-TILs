a,b = input().split()
c,d = input().split()
e,f = input().split()

#체온 b d f
b = int(b)
d = int(d)
f = int(f)

if (a == "Y" and b >= 37) :
    if (c == "Y" and d >= 37) or (e == "Y" and f >= 37)  :
        print("E")
    else :
        print("N")
else :
    if (c == "Y" and d >= 37) and (e == "Y" and f >= 37) :
        print("E")
    else:
        print("N")