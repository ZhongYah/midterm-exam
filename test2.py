g = int(input())

total = 0.65*g
if g >= 200:
    total = total*0.9
else:
     total = total

print(f'{int(total):}元')