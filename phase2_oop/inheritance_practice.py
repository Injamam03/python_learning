"""class Calculator:
    Super Class to define addition, subtraction, multiplication and division.
    def addition(self, x, y):
        return x + y
    def subtraction(self, x, y):
        return x - y
    def multiplication(self, x, y):
        return x * y
    def division(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'

class SubCalculator(Calculator):
    Child class define. To calculate square and cube.
    def square(self, x):
        return x * x

    def cube(self, x):
        return x * x * x


my_calculator = SubCalculator()
temp = my_calculator.addition(60, 30)
print("X+Y:", temp)
temp = my_calculator.subtraction(60, 30)
print("X-Y:", temp)
temp = my_calculator.multiplication(60, 30)
print("X*Y:", temp)
temp = my_calculator.division(60, 30)
print("X/Y:", temp)
temp = my_calculator.square(9)
print("Square of 9:", temp)
temp = my_calculator.cube(5)
print("cube of 5:", temp)"""


class student:
     def __init__(self,name , roll, mark):
          self.name = name
          self.roll = roll
          self.mark = mark 

     def show(self):
        print("Name"+ self.name)
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
     
















    