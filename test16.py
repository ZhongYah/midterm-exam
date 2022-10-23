chinese = int(input())
english = int(input())
math = int(input())

total = (chinese + english + math)/3
if chinese >= 90 and total >= 90:
    print("符合資優生標準")
else:
     print("不符合資優生標準")