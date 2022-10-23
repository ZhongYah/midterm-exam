c = int(input())
e = int(input())
m = int(input())
s = int(input())
n = int(input())

total = c + e + m + s + n

if 460 <= total <= 500:
    print("A")
elif 420 <= total <= 459:
    print("B")
elif 370 <= total <= 419:
    print("C")
elif 320 <= total <= 369:
    print("D") 
else:
    print("E")           
