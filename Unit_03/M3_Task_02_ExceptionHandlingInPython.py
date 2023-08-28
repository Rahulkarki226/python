# Exception Handling
'''
#Exception,Error,Compilation Issues
1. Compilation Issues:
   -Syntax Issues, or issues in the code.
   catch by the python compiler
   pritn("kjskjfkd")
2. Exceptions:
    -Issues in your code,catch by PVM [Python Virtual Machine]
    -Run time issues, Handle [PVM]
    a=10
    b=0
    print(a/b)
    -Handling is possible by using try and except
    -Exceptions   are always handled by the programmer
3. Errors:
   -Can not be handled by the programmer
   -happen at run time
   -Even PVM can not catch them
   Memory full, Stack overflow, power failure etc.
   -System Design should be robust and Efficient
'''
import os
path=os.path.dirname(__file__)
print(path)
path =path+"/"
# try: 
#     #We have to write suspicious code in python
#     file = open(path+"abc.txt",'w')
#     file.write("321")
#     a=int(input("Enter a:"))
#     b=int(input("Enter b:"))
#     c=a/b
   
# except ZeroDivisionError:
#     # Handling of those exceptions
#     print("b should not be zero")
#     b=int (input("Enter b:"))
#     c=a/b

# else:
#     # Handling of above exceptions
#     print("Else block of code")
#     print(c)

# finally:
#     #this block of code will always be executed
#     file.close()
#     print("file is closed now")

# #Rest of the code:
# print("Hello world")
# print("Hello world")
# print("Hello world")
# print("Hello world")
# print("Hello world")
# print("Hello world")

#Raise your own exception

x=int (input("Enter the value X:"))
try:
    if x<0:
        raise Exception
except Exception:
    print("You should not take  x negative")
    x=int(input("Enter the value of x:"))
else:
    print("X:",x)
finally:
     #close your file and database
     print("hello")




