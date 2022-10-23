age = int(input())
money = int(input())

total = money
if 17 <= age < 24:
    total -= 300 
elif 60 <= age < 80:
    total -= 500

print(f'{total:,}元')
