arr = map(int, input().split())
num = 0
total = 0
for i in arr:
    if i >= 250:
        break
    else:
        num+=1
        total+=i

    
print(f"{total} {total/num:.1f}")