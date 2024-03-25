n = int(input())
arr = list(map(int, input().split()))

count = [0 for _ in range(9)]

for ele in arr:
    count[ele-1] +=1

for i in range(1,10):
    print(count[i-1])