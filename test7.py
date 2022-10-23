salary = int(input())
time = int(input())

total = salary*time

if time >= 50:
    total += time*35
elif 30 <= time < 50:
    total += time*25
elif 10 <= time < 30:
    total += time*10
else:
     total += 0

print(f'{total:,}元')
