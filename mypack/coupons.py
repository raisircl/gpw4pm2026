import random
coupons = ["SAVE10", "FREESHIP", "WELCOME"]
it=iter(coupons)

def get_coupon():
    return next(it)

def coupon_generator() :
    print( 'First coupon discount:' )
    yield random.randrange(10, 50, 5)
    print( ' Second coupon discount:' )
    yield random.randrange(10, 50, 5)
    print( 'Last coupon discount:')
    yield random.randrange(10, 50, 5)
        