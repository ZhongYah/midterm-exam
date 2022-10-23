coupon = str(input())

if coupon[0] in ("1", "3", "7", "8") and coupon[1] in ("3", "5", "9") or coupon[-1] == "0":
    print("中獎")
else:
     print("沒中獎")

