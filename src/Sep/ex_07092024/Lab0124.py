# Method Overriding-> Child or Subclass, can have same name method as the Parent/ Super class


class Shape:
    def area(self):
        print("Print the area of the shape: ")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius

shape1 = Rectangle(3,4)
print(shape1.area())

shape2 = Circle(3)  # line 15 will get print in this case bcz local has the more prefernce

print(shape2.area()) # line 23 will get print in this case bcz local has the more prefernce, however if line 22 and 23 are not present then None will get print with above print stmnt