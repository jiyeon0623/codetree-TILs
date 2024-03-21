a,b,c = map(int, input().split())
satisfied = True

for i in range(a,b+1):
    if i % c != 0:
        satisfied = False
if not satisfied:
    print("NO")
else:
    print("YES")