seat = str(input())
number = int(input())

if seat in ("A"):
    total = number*500
else:
     total = number*300

print(f'{total:,}元')