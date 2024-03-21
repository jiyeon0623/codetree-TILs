n = int(input())
sum = 0
for i in range(n):
    sum+=int(input())

print("{} {:.1f}".format(sum, sum/n))