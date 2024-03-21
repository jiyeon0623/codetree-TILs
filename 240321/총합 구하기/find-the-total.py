a,b = input().split()
sum = 0
a,b = int(a), int(b)
for i in range(a,b+1):
    if ( i %6 ==0 and i %8 !=0):
        sum +=i

print(sum)