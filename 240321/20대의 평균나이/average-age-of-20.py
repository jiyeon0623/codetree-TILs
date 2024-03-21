sum = 0
cnt = 0

while True:
    p = int(input())
    if p//10 !=2:
        print("%.2f"%(sum/cnt))
        break
    sum+=p
    cnt+=1