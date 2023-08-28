#convert H2O to H₂O using maketrans and translate method of string.
from email.policy import default

s="H2O"
subscript= str.maketrans("0123456789","₀₁₂₃₄₅₆₇₈₉")
p=s.translate(subscript)
print(p)

#using match and case give the status of student in a Exam.
Marks=int(input("Enter the Marks:"))
ch=0
if(Marks<30):
    print("Fail")
elif(Marks==30):
    print("Pass but bad score")
elif(Marks>=40 and Marks<50):
    print("Ok")
elif(Marks>=50 and Marks<60):
    print("OK OK")
elif(Marks>=60 and Marks<75):
    print("First Class")
else:
    print("First Class with 'D'")

        
    

