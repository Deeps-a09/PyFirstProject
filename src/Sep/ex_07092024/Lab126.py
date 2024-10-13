# Method Overloading

class MathUtil(object):  #By default in Python "object" is a father of every class

# Method Overloading is not supported in python
  def add(self,a,b):
      return a + b
  def add(self,a,b,c=0):
      return a+b+c
math = MathUtil()
op1= math.add(1,2)
print(op1)