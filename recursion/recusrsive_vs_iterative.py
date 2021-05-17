#recursive
def twotopower(n):
    if n == 0:
        return 1
    else:
        pot = twotopower(n - 1)
        return pot * 2
# in  out
#4 power = twotopower(3)
#3 power = twotopower(2)
#2 power = twotopower(1)
#1 power =  twotopower(0)


#iterative
def powerOfTwoIt(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i+=1
    return power
print("start")
print(twotopower(3))


