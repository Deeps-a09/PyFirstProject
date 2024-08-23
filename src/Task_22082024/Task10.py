"""
Task #10 -
✅ Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

Logic:
1: factorial = 1 * 1 = 1
2: factorial = 1 * 2 = 2
3: factorial = 2 * 3 = 6
4: factorial = 6 * 4 = 24
5: factorial = 24 * 5 = 120
"""

num = int(input("Enter the number: "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print(f"Factorial of {num} is {factorial}")
