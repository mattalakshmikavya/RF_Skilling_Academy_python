## 4.Develop a Python script that calculates and prints
#  the result of raising a user-input base to a user-input exponent
#  without using the ** operator.


base=int(input("enter the base number"))
exponent=int(input("enter the exponent"))

result=1

for i in range(exponent):
    result=result*base


print("result:", result)
