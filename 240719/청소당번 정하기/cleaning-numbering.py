n = int(input())
ent2 = 0
ent3 = 0
ent12 = 0

for i in range(1,n+1):
    if i % 12 ==0 :
        ent12 += 1  
    elif i %3 == 0 :
        ent3 += 1
    elif i %2 == 0: 
        ent2 += 1
print(ent2, ent3, ent12)