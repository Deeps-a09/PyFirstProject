"""
Task #11 -
✅ Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13


"""

n = int(input("Enter Number: "))
a = 0
b = 1
print(a, b, end=" ")
for i in range(1, n):
    c = a + b
    print(c, end=" ")
    a = b
    b = c
