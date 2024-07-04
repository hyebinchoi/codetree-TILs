a,b = input().split()
c,d = input().split()
e,f = input().split()

#체온 b d f
b = int(b)
d = int(d)
f = int(f)



if (a == "Y") :
    if (b >= 37) :
        "A"
    else :
        "C"
elif (a == "N"):
    if (b >= 37) :
        "B"
else :
    "D"

if (c == "Y") :
    if (d >= 37) :
        "A"
    else :
        "C"
elif (c == "N"):
    if (d >= 37) :
        "B"
else :
    "D"

if (e == "Y") :
    if (f >= 37) :
        "A"
    else :
        "C"
elif (e == "N"):
    if (f >= 37) :
        "B"
else :
    "D"

if count("A") >= 2 :
    print("E")
else :
    print("N")