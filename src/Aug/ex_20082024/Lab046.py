# ✅ Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:
#
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

score = int(input("Enter score: \n"))
grade = "F"
if 90 <= score <= 100:
    grade = "A"
    print(f"Your grade is {grade}")
elif score >= 80 and score <= 89:
    grade = "B"
    print(f"Your grade is {grade}")
elif score >= 70 and score <= 79:
    grade = "C"
    print(f"Your grade is {grade}")
elif score >= 60 and score <= 69:
    grade = "D"
    print(f"Your grade is {grade}")
elif score > 100 and score <= 0:
    print("Your are a superwoman!")
else:
    grade = "F"
    print(f"Your grade is {grade}")
