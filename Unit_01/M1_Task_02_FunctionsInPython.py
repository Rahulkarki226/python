# M1_Task-02_FunctionsInPython.py

import py_compile


def my_function():
  print("Hello from a function")
print("Out of the function")

my_function()

# Function with parameter (python does not allow "int + String")
def my_function(fname):
  print(str(fname) + " Reference")

my_function("Emil")
my_function("Password")
my_function(123)
my_function(1)
my_function(1.2)



def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Password")


#Arbitrary Arguments, *args
def my_function(*kids):
  print(kids[2])

my_function("Ravi", "Sumit", "Amit")
my_function("Ravi", "Sumit", "Amit", "Ankush")
#my_function("Ravi", "Sumit") #tuple index out of bound issue
my_function("Ravi",123,123.4,'A')


#Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emi", child2 = "Amit", child3 = "Ravi")




#Default value of function parameter
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


#Passing a List as an Argument [iterator object, list*]
def my_function(food):
  for i in food:
    print(i)

fruits = ["apple", "banana", "cherry", 123, 123.4]

my_function(fruits)


#Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9.2))

# Pass function
def myfunction():
  pass

myfunction()