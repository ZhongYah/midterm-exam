number = int(input())

if number >= 100000:
    total = number*0.215
else:
     total = number*0.165

print(f'{int(total):,}元')