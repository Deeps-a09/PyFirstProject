# Find max between three number
# when we have more than one condition, we use 'if elif else'
"""
if condition 1:
 print("do 1")
elif condition 2:
   print("do 2")
 else:
   print("do 3")
"""

a = int(input("Enter first number: \n"))
b = int(input("Enter second number: \n"))
c = int(input("Enter third number: \n"))

if a > b and a > c:
    print(f"Max is {a}")
elif b > a and b > c:
    print(f"Max is {b}")
else:
    print(f"Max is {c}")
