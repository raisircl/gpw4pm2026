from mypack import coupons

coupon = coupons.get_coupon()
print(f"Your coupon code is: {coupon}")

coupon = coupons.get_coupon()
print(f"Now Your coupon code is: {coupon}")

gen = coupons.coupon_generator()
discount = next(gen)
print(f"Your discount is: {discount}")

discount = next(gen)
print(f"Your discount is: {discount}")

discount = next(gen)
print(f"Your discount is: {discount}")
