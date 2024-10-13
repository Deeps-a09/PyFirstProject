#create a program of sum of three input numbers

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
num3 = int(input("Enter the num3: "))

def sum_of_three_num(n1,n2,n3):
    return n1 + n2 + n3
result = sum_of_three_num(num1, num2, num3)
print(result)

#result = sum_of_three_num(n1=num1, n2=num2, n3=num3)
#print(result)