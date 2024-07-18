n = int(input())
ent2 = 0
ent3 = 0
ent12 = 0

for i in range(0,n):
    if i>=2 and i %2 == 0:
        ent2 += 1
    if i>=3 and i %3 == 0 :
        ent3 += 1
    if i>=12 and i %12 ==0 :
        ent12 += 1
print(ent2, ent3, ent12)