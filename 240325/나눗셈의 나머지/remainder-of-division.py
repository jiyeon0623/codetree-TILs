a,b = input().split()
a,b = int(a), int(b)
cnt = [0]*b

while True:
    if a<=1:
        break
    a = a//b #몫
    add = a%b  #나머지
    cnt[add] +=1

sum = 0
for elem in cnt:
    sum +=elem**2

print(sum)