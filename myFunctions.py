

def bunchOfCode(value) :
    if( value > 100) :
        print("bigger than 100")
    else :
        print("not bigger than 100")

def sayLotsOStuff():  #function header
    print("Lots of")
    print("Stuff")

sayLotsOStuff()     #called the function
sayLotsOStuff()

def sayThree(parameter):
    print(parameter)
    print(parameter)
    print(parameter)

sayThree("howdy")
sayThree(42)

def cubeIt( num):
    return num * num * num

print(cubeIt(4))

def guess(param):
    return param * 3 + 2

print(guess(87))
print(guess(100))

import math

print(math.floor(3.78))
print(math.ceil(5.12))
print(math.pow(2,7))
print(math.fabs(-9))
print(math.sqrt(256))
