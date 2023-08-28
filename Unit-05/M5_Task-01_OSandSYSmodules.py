import os
import sys
#get the current working directory(cwd)
cwd=os.getcwd()
print("Current working directory:",cwd)

#changing the current working directory
def current_path():
    print("current working directory befor:")
    print(os.getcwd())
    print()

current_path()
#changing the cwd4
os.chdir("../")
#printing cwd after change
current_path()

#making your own directory
#directory
#directory="Python_workspace"
#parent_dir=os.getcwd()
#path=os.path.join(parent_dir,directory)
#os.mkdir(path)

#remove a file
#file="abc.txt"
#path=os.path.join(parent_dir,file)
#os.remove(path)

#removing directory [dont run in source code folder]
#directory="kajal"
#path=os.path.join(parent_dir,directory)
#os.rmdir(path)

'''the sys module in python provides various functions and variables the are 
used to maniuplate different parts of the python runtime environment.
-sys.version is used which returns a string containing the version of python
 interpreter with some additional information.
-this shows how the sys module interacts with the interpreter.
'''
#input and output using sys
'''
stdin
-it can be used to get input from the command line directly.
-it ,also automatically adds '\n' after each sentence.
'''
import sys
for line in sys.stdin:
    if 'q'==line.rstrip():
        break
    print(f'Input : {line}')

print("Exit")

'''#stdout
-A built in file object that is anlogous to the interpreter standard
 output stream in python.
-stdout is used to display output directly to the screen console'''
import sys 
sys.stdout.write("jhrfuei fef ")
sys.stdout.write("jhrfuei fef ")
sys.stdout.write("jhrfuei fef ")
sys.stdout.write("jhrfuei fef ")
sys.stdout.write("jhrfuei fef ")
 #o/p: jhrfuei fefjhrfuei fefjhrfuei fefjhrfuei fefjhrfuei fef
#sys.stdout.write("jhrfuei fef") similar to print("jhrfuei fef ",end=" ")
print("jhrfuei fef ",end=" ")
print("jhrfuei fef ",end=" ")
print("jhrfuei fef ",end=" ")
print("jhrfuei fef ",end=" ")
print("jhrfuei fef ",end=" ")

'''# sys.argv
command line arguments:
-command-line arguments are those'''