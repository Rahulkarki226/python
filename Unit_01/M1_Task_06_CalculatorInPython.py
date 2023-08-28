# Create a calculator in python 
# and along with that test all the functionalities you have created

def add(a,b):
    return (a+b)

def sub(a,b):
    return (a-b)

def multi(a,b):
    return (a*b)

def div(a,b):
    return (a/b)

def expo(a,b):
    return a**b

def floorDiv(a,b):
    return a//b


def main():
    if add(10,20) == 30:
        print("add functionality is working fine\n")

    if sub(30,20) == 10:
        print("sub functionality is working fine\n")

    if multi(3,6) == 18:
        print("multi functionality is working fine\n")

    if div(40,20) == 2:
        print("div functionality is working fine\n")

    if expo(2,2) == 4:
        print("expo functionality is working fine\n")
    
    if floorDiv(5,2) == 2:
        print("floorDiv functionality is working fine\n")


if __name__ == "__main__":
    main()
