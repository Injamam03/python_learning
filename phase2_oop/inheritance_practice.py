
class Calculator:
    def addition(self, x, y):   
        return x + y
    def subtraction(self, x, y):   
        return x - y
    def multiplication(self, x, y): 
        return x * y
    def division(self, x, y):
        try:    return x / y
        except ZeroDivisionError: 
            return 'Cannot divide by zero.'

class SubCalculator(Calculator):
    def square(self, x): 
        return x * x
    def cube(self, x):   
        return x * x * x

result = SubCalculator()

print("X+Y:", result.addition(60, 30))
print("X-Y:", result.subtraction(60, 30))
print("X*Y:", result.multiplication(60, 30))
print("X/Y:", result.division(60, 5))
print("Square of 9:", result.square(9))
print("cube of 5:", result.cube(5))
















"""

class Calculator:
    def addition(self, x, y):      return x + y
    def subtraction(self, x, y):   return x - y
    def multiplication(self, x, y): return x * y
    def division(self, x, y):
        try:    return x / y
        except ZeroDivisionError: return 'Cannot divide by zero.'

class SubCalculator(Calculator):
    def square(self, x): return x * x
    def cube(self, x):   return x * x * x


c = SubCalculator()
print("X+Y:", c.addition(60, 30))
print("X-Y:", c.subtraction(60, 30))
print("X*Y:", c.multiplication(60, 30))
print("X/Y:", c.division(60, 0))
print("Square of 9:", c.square(9))
print("cube of 5:", c.cube(5))
"""


"""class student:
     def __init__(self,name , roll, mark):
          self.name = name
          self.roll = roll
          self.mark = mark 

     def show(self):
        print("Name = " + self.name)
        # print(f"Name = {self.name}")
        print(f"Roll = {self.roll}")
        print(f"Mark = {self.mark}")
        print("-------------------")
s1 = student("Injamam",20,50)
s2 = student("Shawon",10,40)
s3 = student("monir",60,30)

s1.show()
s2.show()
s3.show()






#  next time same program practice 
class student:
    def __init__(self, name , roll, mark):
        self.name = name
        self.roll = roll
        self.mark = mark
    def show(self):
            print("Name = " + self.name)
            print("Roll = " + self.roll)
            print("mark = " + self.mark)
s1=student("Injamam",20,30)
s2=student("shawon",20,30)
s3=student("rakib",20,30)

s1.show()
s2.show()
s3.show()"""



        
     
















    