seat = str(input())
amount = int(input())

if seat in ("A", "C", "E", "F", "K"):
    total = 350*amount
else:
     total = 550*amount

print(f'{total:,}元')


