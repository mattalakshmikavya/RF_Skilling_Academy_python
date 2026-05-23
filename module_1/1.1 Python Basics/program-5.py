## 5. Write a program that takes coefficients of a quadratic equation 
# as input and solves for the roots. Handle both real and complex roots.

a=int(input("enter a:"))
b=int(input("enter b:"))    
c=int(input("enter c:"))    
d=b**2-4*a*c
if d>0:
    print("the roots are real and different")
else:
    if d==0:
        print("the roots are real and same")
    else:
        print("the roots are complex")  