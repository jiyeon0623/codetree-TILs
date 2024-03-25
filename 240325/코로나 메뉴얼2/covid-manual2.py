new_arr = [0] * 4
for i in range(3):
    arr = input().split()
    
    if arr[0] == 'Y':
        if int(arr[1]) >=37:
            new_arr[0]+=1
        else:
            new_arr[2]+=1
    else:
        if int(arr[1]) >=37:
            new_arr[1]+=1
        else:
            new_arr[3]+=1

if new_arr[0]>=2:
    new_arr.append("E")

for elem in new_arr:
    print(elem, end = " ")