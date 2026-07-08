class Student:
    def __init__(self, name, mark):
        self.name = name
        self.__mark = mark      # It's hidden 

    def get_mark(self):
       print(f"Name: {self.name}")    
       print(f"Mark: {self.__mark}")
       
s1 = Student("Injamam", 95)
s1.get_mark()           # Right way 
  