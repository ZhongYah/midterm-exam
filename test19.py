number = int(input())
score = int(input())
license = str(input())

if number >= 3 and license == "Y" or score > 500:
    print("符合面試條件")
else:
     print("不符合面試條件")

     