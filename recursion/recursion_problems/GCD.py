def gcd(x,y):
    assert int(x) == x and int(y) ==y, "INT Must be int"
    if x < 0:
        x = -1 * x
    if y < 0:
        y = y*-1
    if y == 0:
        return x
    else:
        return  (gcd(y,(x%y)))





print(gcd(20,8))