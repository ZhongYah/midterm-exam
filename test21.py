coupon = str(input())
price = int(input())
amount = int(input())

total = price*amount
if coupon == "A":
    if total >= 3000:
        total *= 0.8
    elif total >= 2000:
         total *= 0.9
    else:
         total *= 0.95
elif coupon == "B":
    if total >= 4000:
        total *= 0.75
    elif total >= 3000:
        total *= 0.85
else:
     if coupon == "C":
        total *= 0.9

print(f'{int(total):,}元')
