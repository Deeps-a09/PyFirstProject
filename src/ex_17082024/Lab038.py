"""
Task- 4 Write a Python program to calculate the area of a circle given its radius using the formula ``` area=π×r^2```
( Take pie as 3.14)
"""
import math

r = float(input("Enter the radius of the circle"))
print(r)
#area = 3.14 * (r ** 2)
area = math.pi * math.pow(r,2)
print(area)