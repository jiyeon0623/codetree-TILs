n = int(input())
count = 0
for _ in range(n):
    arr = map(int, input().split())
    avg = sum(arr)/4
    if avg>= 60:
        print("pass")
        count+=1
    else:
        print("fail")

print(count)