cnt = 0;
n = int(input())

for i  in range(n+1):
    if (i %4 == 0 and i % 100 !=0) or i %400== 0:
        cnt +=1

print(cnt)