a,b,c = input().split()
a,b,c = int(a), int(b), int(c)

bool1 = False
for i in range(a,b+1):
    if i % c == 0:
        bool1 = True

if bool1:
    print("YES")
else:
    print("NO")