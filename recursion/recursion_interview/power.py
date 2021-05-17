#Problem: use recursion to determine the power of a number



def power_calc(base,exponent):
    if exponent == 0:
        return 1
    else:
        return base * power_calc(base,(exponent-1))


print(power_calc(11,12))