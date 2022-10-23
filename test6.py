from re import S


set = str(input())
number = int(input())

if set == "A":
    total = number*500
elif set == "B":
    total = number*450
elif set == "C":
    total = number*380
elif set == "D":
    total = number*310
elif set == "E":
    total = number*250

print(f'{total:,}元')