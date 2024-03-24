n = int(input())
arr = map(float, input().split())

grade = sum(arr)/n

print(f"{grade:.1f}")

if grade >=4.0:
    print("Perfect")
elif grade >= 3.0:
    print("Good")
else:
    print("Poort")