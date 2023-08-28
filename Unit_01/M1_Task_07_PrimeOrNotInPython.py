# M1_Task-07_PrimeOrNotInPython

# o(n)
import math
from re import A

def primeOrNor1(x):

    count = 0
    y = int(x)
    for i in range(2,y-1):
        if y%i == 0:
            count = count + 1

    if count == 0:
        return "Yes it a prime number"

    else:
        return "Not a prime"

# o(n/2)
def primeOrNor2(x):

    count = 0                             
    y = int(x)
    for i in range(2,y//2):
        if y%i == 0:
            count = count + 1

    if count == 0:
        return "Yes it a prime number"

    else:
        return "Not a prime"


# o(sqrt(n))
def primeOrNor3(x):

    count = 0
    y = int(x)
    r = math.ceil(math.sqrt(y)) # sqrt1(y)
    print(r)
    for i in range(2,r+1):
        if y%i == 0:
            count = count + 1

    if count == 0:
        return "Yes it a prime number"

    else:
        return "Not a prime"           


def sqrt1(x):

    i = 1
    r = 1
    while(r < x):
        r = i*i
        i=i+1

    return i-1

def primeOrNor4(x):

    count = 0
    y = int(x)
    r = sqrt1(y)
       
    for i in range(2,r+1):
        if y%i == 0:
            count = count + 1

    if count == 0:
        return "Yes it a prime number"

    else:
        return "Not a prime" 

x = input("Enter the value of x: \n")
primeOrNor1(x)
# primeOrNor2(x)
# primeOrNor3(x)
# primeOrNor4(x)