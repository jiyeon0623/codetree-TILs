a,b = input().split()
a,b = int(a), int(b)
bool1= False
for i in range(a,b+1):
    if (1920 % a == 0 and 2880 %a == 0):
        bool1 = True
    
if bool1:
    print(1)
else:
    print(0)