arr = list(map(int, input().split()))

for i in range(10):
    add_arr = arr[i+1]+ 2*arr[i]
    arr.append(add_arr)
    print(arr[i], end = " ")