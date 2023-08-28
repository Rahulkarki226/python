#George

'George'

"George"

print ('George')

print ("George")

x4 = "George"

""
''
""""""
''''''

x4

# y = 10
#print (y + "Dollars")

y = 10
print (str(y) + " Dollars")

#'I'm fine'

"I'm fine"

# Escape a character
'I\'m fine'

'Press "Enter"'

'Red' 'car'

'Red ' 'car'

'Red ' + 'car'  # concating two strings in python

print ('Red ' + 'car')

print ('Red', 'car', 123)

print (3,5)

3, 5, 6.9, 7.0, 'car'


'''
Syntax:
    slice(stop)
    slice(start, stop, step)
'''

# String slicing
String = 'ASTRING'

# ASTRING
# 0123456
# -7-6-5-4-3-2-1
 
# Using slice constructor
# print("String slicing")
# print(String[slice(3)])
# print(String[slice(1, 5, 2)])
# print(String[slice(-1, -8, -2)])

# print(String[-2])


'''
Syntax:
    s[index]
    s[start, stop]
    s[start, stop, step]
'''
String = 'ASTRING'
String[0]
String[2::]
String[::2]
String[:4:]
String[-4:-1]
String[-1:-4:-1]

# Repeating a string
print((String+'\n') * 10)
print(123 * 10)















# '''''' and """""" can also be used to represent a string

s = """Hello World""" # docstring
print(s)


# String length
l = len(s)
print(l)


# compare two strings
s1= "helloo"
s2= "hello"

if s1 == s2:
    print("Equals")
else:
    print("Not Equals")

if s1 <= s2:
    print("s1 is smaller than or equal to s2")
else:
    print("s2 is smaller than s1")


# Removing space from the string
name = " Akash Chauhan "
print(name.rstrip())
print(name.lstrip())
print(name.strip()) # Remove both left and right spaces from the string
print(name)







# Find a substring
str = input("Enter main string: ")
subStr = input("Enter sub string: ")

n = str.find(subStr,0,len(str))

if n == -1:
    print("Substring not found")
else:
    print("Substring found at position",n)






# Strings are Immutable in Python: 
"""
An immutable object is a object whose content can not be changed
In python: strings, numbers and tuples are immutable
"""

s1 = 'one'
s2 = 'two'

s1 = s2

print(s1)


# Replacing a substring
str = "That is beautiful"
s1 = 'beautiful'
s2 = 'not beautiful'

str1 = str.replace(s1,s2)
print(str1)







# Converting strings to numbers 
str = "25"
number = int(str)
print(number)

# Converting numbers to strings
str2 = str(number)
print(str2)



# Split function 
str = "That is beautiful"
str1 = str.split(' ')
print(str1) 

for i in str1:
    print(i)



# changing case of a string
str = "That is beautiful"
print(str.upper())
print(str.lower())
print(str)









# Superscript and Subscript concept in Python
numbers_to_letters = str.maketrans("123", "ABC")
print("Question 1, point 2 and 4".translate(numbers_to_letters))

# subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
# print("C2H5OH".translate(subscript))

# superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
# print("PIr2".translate(superscript))

# superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
# print("PIr2".translate(superscript).replace('PI', 'π'))
