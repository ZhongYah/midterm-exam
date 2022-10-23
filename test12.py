from curses import ALL_MOUSE_EVENTS


number = str(input())
amount = int(input())

if number[0] not in ("T", "M","L", "N"):
    total = 500*amount
else:
     total = 400*amount

print(f'{total:,}元')