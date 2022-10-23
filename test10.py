number = int(input())
amount = int(input())

if number%3 != 0:
    total = 500*amount
else:
     total = 400*amount

print(f'{total:,}元')