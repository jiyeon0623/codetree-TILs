c,n = input().split()
n = int(n)
i =1

if c == "A":
    for _ in range(n):
        print(i, end = " ")
        i+=1
else:
    for _ in range(n):
        print(n, end =" " )
        n-=1