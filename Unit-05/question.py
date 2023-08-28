#program to find all the word ends with vowel
#program to find all the word starting with digit
# import re
# txt="the rahul don i here keanu and on"
# print(re.findall("\S*[aeiouAEIOU]\\b",txt))
# con="1rah 4djld jlfkdj fldkhf fdklsooa 6"
# print(re.findall("\\b[0-9]\S*",con))
# write a program to fetch a date from a string and make sure  14.06.2012
# wap to fetch all the words which start with a capital letter
# program fetch a string that has a

'''
-By default, the print function ends with a newline.
-Passing the whitespace to the end parameter(end=' ') indicates
 that the end character has to be identified by white space and
 not a new line.
'''

#Q1
'''
-WAP in python to check if the entered number is prime or not
using command line argument technique
 
 Also use square root technique to check if it is prime or not!
'''
import sys
import math
def primeornot(l):
    value=math.ceil(math.sqrt(l))+1
    for i in range(2,value):
        if l%i==0:
            return "Not Prime"
    return "Prime"

result =primeornot(int(sys.argv[1]))
print(result)