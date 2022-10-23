number = str(input())

if number[0] in ("A", "F", "K"): 
    if number[8:10] in ("21", "32", "50"):
        print(f'{5000:,}元')
    elif number[8:10] in ("43", "66", "89"):
        print(f'{4000:,}元')
    elif number[8:10] in ("85", "10", "12"):
        print(f'{3000:,}元')
    else:
         print(f'{0:,}元')

elif number[0] in ("M", "P", "Q"): 
    if number[8:10] in ("45", "61", "23"):
        print(f'{5000:,}元')
    elif number[8:10] in ("89", "77", "32"):
        print(f'{4000:,}元')
    elif number[8:10] in ("24", "54", "36"):
        print(f'{3000:,}元')
    else:
         print(f'{0:,}元')

elif number[0] in ("R", "U", "V"): 
    if number[8:10] in ("76", "90", "21"):
        print(f'{5000:,}元')
    elif number[8:10] in ("56", "81", "50"):
        print(f'{4000:,}元')
    elif number[8:10] in ("20", "31", "41"):
        print(f'{3000:,}元')
    else:
         print(f'{0:,}元')

else:
     print(f'{0:,}元')

