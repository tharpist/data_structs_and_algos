def firstMethod():
    secondMethod()
    print("First")

def secondMethod():
    thirdMethod()
    print("Second")

def thirdMethod():
    fourthMethod()
    print("third")

def fourthMethod():
    print("fourth")


firstMethod()
#Last in first out strategy is the way a stack handles 
print("yolo")