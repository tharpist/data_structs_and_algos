#Fibonacci sequence is a sequence of numbers in 
# which each number is the sum of the two preceding ones 
# and the seqience starts from 0 and 1


def fibonacci(n):
    #constraint
    assert n>=0 and int(n) == n, 'the number can only be positive and must be int'
   #base case
    if n in [0,1]:
        return n
    #recursion
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(6))