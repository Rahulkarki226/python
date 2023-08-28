#sys.argv
'''
#sys.argv:command line arguments:
-Command-line arguments are those which are passed
 during the calling of the program along with the
 calling statement.
'''
# benefit-program didn't hold for the user input
import sys
#total arguments
n=len(sys.argv)
print("Total arguments passed:",n)

#Arguments passed
print("\nName of python script:",sys.argv[1])

print("\n Aruguments passed:",end=" ")
for i in range(1,n):
    print(sys.argv[i],end=" ")

#Addition of numbers
sum=0

for i in range(1,n):
    sum+=int(sys.argv[i])

print("\n\nResult:",sum)
