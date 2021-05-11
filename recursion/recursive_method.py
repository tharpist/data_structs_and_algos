def recursiveMthod(n):
    if n<1:
        print("n is less than 1")
    else:
        recursiveMthod(n-1)
        print(n)




print("START")
recursiveMthod(4)



#Stack gets created
#Function gets called every time
# LIFO-> Last in First Out== FILO
#4 goes into stack 

# STACK
# recursiveMethod(0) -> n is less than 1
#
# recursiveMethod(1) -> 1
#----------------------------
# recursiveMethod(2) -> 2
#----------------------------
# recursiveMethod(3) -> 3
#-----------------------------
# recursiveMethod(4) ->4
#-----------------------------
#https://stackoverflow.com/questions/61775669/is-filo-always-lifo