# Q1. Write a Python program to read first n line of a file?
# import os
# path=os.path.dirname(__file__)
# path=path+'/'

# def flines(file,n):
#     lines=file.readlines()
#     lines=lines[:n:]#list is mutable
#     for line in lines:
#         print(line,end='')

# file=open(path+'abc.txt','r')
# n=int(input("Enter n:"))
# flines(file,n)

# Q2. Write a python program to read last n line of a file?
# def lastl(file,n):
#     lines=file.readlines()
#     length=len(lines)
#     lines=lines[length-n::]
#     for line in lines:
#         print(line)
# file=open(path+'abc.txt','r')
# n=int(input("Enter n:"))
# lastl(file,n)


# # Q3. Write a python program to find the longest word?
# def longestWordsInafile(file):
#       allwords=[]
#       data=file.readlines()
#       for i in data:
#             words=i.split()
#             allwords=allwords+words
#       maxlength=0 
#       for i in allwords:
#             if(len(i)>maxlength):
#                   maxlength=len(i)
#       for i in allwords:
#             if maxlength==len(i):
#                   print(i)

# # file=open(path+"abc.txt","r")
# # longestWordsInafile(file)

# #Q4 .WAP to handle file not found exception?
# def openAFile(path,str):
#       try:
#             file=open(path+str,"r")
#       except FileNotFoundError:
#             print("Exception is handled")
#             file=open(path+str,"w+")
#       return file
# print("=====================")
# file=openAFile(path,"abcd.txt")
# file.write("jdsjljldj")
# file.close()

# Q5. When to write try, except, else and finally,
#    Wap to explain your answer?
# In Python, the try statement is used to enclose a block of code that may 
# raise an exception. If an exception is raised within the try block, the code
#  in the corresponding except block(s) will be executed. The else block, if present,
#   will be executed if no exceptions were raised in the try block. And finally block
#    will execute always after try-else block whether exception occured or not.

#Q6. WAP to find unique number of words in a file?
# file=open(path+"abcd.txt","r+")
# s=set()
# paragraph=file.readlines()
# for sentence in paragraph:
#       words=sentence.split()
#       for word in words:
#             s.add(word)
# print(s)


#Q7.WAP to handle a None type Exception handling in python!
# def divide(a,b):
#     try:
#         if a is None or b is None:
#             raise Exception
#     except Exception:
#           print("input cannot be none")
#     else:
#         return a/b

# a=None
# b=2
# print(divide(a,b))

#Q8.Write a python program to get the file size of a plain file.
# import os
# path=os.path.dirname(__file__)
# path=path+'/'
# def getsize(fp):
#     filesize= os.path.getsize(fp)
#     print("Total size of file:",filesize)

# fp=path+"abc.txt"
# getsize(fp)






