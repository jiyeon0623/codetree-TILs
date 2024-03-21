n = int(input())
i = 1
while True:
    if n == 2**i:
        print(i)
        break
    else:
        i+=1