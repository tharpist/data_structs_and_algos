#Problem: find sum of digits of each digit in a positive int.


def sum_digits(x):
    assert x>=0 and int(x) == x, 'the number can only be positive and must be int'    
    if x <= 10: 
        return x
    else:
        return int(x%10) + sum_digits(int(x//10))



print(sum_digits(678))

#print(55/2)
