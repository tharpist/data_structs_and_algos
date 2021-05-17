def factorial(n):
    assert n>=0 and int(n) == n, 'the number can only be positive'
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)



print(factorial(1))


#things i need for recursion
#base case (makes code stop)
#recursion case
#unintentional case the constraint
