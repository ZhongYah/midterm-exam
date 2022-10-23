height = float(input())
weight = float(input())
second = float(input())

height /= 100

bmi = weight/(height)**2

if 19 <= bmi <= 21 or second <= 13.5:
    print("符合條件")
else:
     print("不符合條件")