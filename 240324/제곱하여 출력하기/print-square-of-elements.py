n = int(input())
arr = list(map(int, input().split()))

arr2= [ele **2 for ele in arr]

for i in range(len(arr2)):
    print(arr2[i], end = " ")