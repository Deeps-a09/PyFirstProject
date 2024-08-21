"""
Create a program that determines whether a given year is a leap year.

A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

Use an if-else statement to make this determination.

Logic:
If a year is evenly divisible by 4, 100, and 400, then it is a leap year.
If a year is divisible by 4 but not by 100 and not divisible by 400, then it is also a leap year.
If a year is not divisible by 4, then it is not a leap year.
If a year is divisible by 4 and 100 but not by 400, then it is not a leap year.
"""

year = int(input("Enter Year: \n"))

if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print(f"{year} is a Leap Year")
elif year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
    print(f"{year} is a Leap Year")
elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
    print(f"{year} is not a Leap Year")
else:
    print(f"{year} is not a Leap Year")
