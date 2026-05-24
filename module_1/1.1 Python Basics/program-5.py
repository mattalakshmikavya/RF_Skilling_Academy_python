## 5. Write a program that takes coefficients of a quadratic equation 
# as input and solves for the roots. Handle both real and complex roots.

a=int(input("Enter a:"))
b=int(input("Enter b:"))    
c=int(input("Enter c:"))

d=b**2-4*a*c

root1=(-b+d**0.5)/(2*a)
root2=(-b-d**0.5)/(2*a) 

print("Root 1=", root1)
print("Root 2=", root2) 