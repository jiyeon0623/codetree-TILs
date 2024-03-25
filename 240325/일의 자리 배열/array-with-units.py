arr = list(map(int, input().split()))

for i in range(10):
    add_arr = (arr[i] + arr[i+1])%10
    
    arr.append(add_arr)
    print(arr[i], end = " ")