chinese = int(input())
english = int(input())
math = int(input())
txt = str(input())

total = (chinese + english + math)/3

if total >= 90 or chinese >= 90 or txt == "A":
    print("符合條件")
else:
     print("不符合條件")

