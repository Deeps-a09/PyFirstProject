"""
Write a program that classifies a triangle based on its side lengths.

Given three input values representing the lengths of the sides,

determine if the triangle is equilateral (all sides are equal),

isosceles (exactly two sides are equal), or scalene (no sides are equal).

Use an if-else statement to classify the triangle.
"""

side1 = float(input("Enter the length of first side: "))
side2 = float(input("Enter the length of second side: "))
side3 = float(input("Enter the length of third side: "))

if side1 == side2 and side1 == side3:
    print("It is an Equilateral Triangle")
elif side1 == side2 and side1 != side3 and side2 != side3:
    print("It is an Isosceles Triangle")
else:
    print("It is an scalene Triangle")
