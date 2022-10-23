d = str(input())
c = int(input())
e = int(input())
m = int(input())

if d == "1":
    total = c*1.5 + e*2 + m*1.5
elif d == "2":
    total = c*2 + e*1.5 + m*1
elif d == "3":
    total = c*1.5 + e*1.5 + m*1
elif d == "4":
    total = c*1 + e*1 + m*2

print(total)