print(" ================  00000000 =======================")

# age= int(input("Enter Your Age : "))

# if(age>=18):
#     print(" your vaild for vote")
# else:
#     print(" your are invaild for vote")

print(" ================  00000000 =======================")

# light = input("light Color : ")

# if (light == "red"):
#     print("Stop and wait for green")

# elif(light == "yellow"):
#     print("wait a moment")
# elif(light=="green"):
#     print("go")
# else:
#     print("light is broken")


print(" ================  00000000 =======================")


# mark = int(input("Enter your marks : "))
# if (mark >=90):
#     print("Your got golden A+")

# elif(mark >=80 and mark<90):
#     print(" your got A+")

# elif(mark >=70 and mark<80):
#     print(" your got A")

# elif(mark >=60 and mark<70):
#     print(" your got B+")

# elif(mark >=50 and mark<60):
#     print(" your got B")

# elif(mark >=40 and mark<50):
#     print(" your got C")
    
# elif(mark >=33 and mark<40):
#     print(" your got D")
# else:
#     print(" you are failed")

print(" ================  00000000 =======================")

# a = int(input("Enter your value of A : "))
# g = input("Male or Female : ")

# if ( (a == 1 or a == 2) and g == "Male"):
#     print("your fee 100")
# elif( a == 3 or a == 4 or g == "Female"):
#     print("your fee 200")
# elif(a == 5 and g == "Male"):
#     print("your fee is 500")
# else:
#     print("no fee your free ")
    

print(" ================  One line if and else condition  =======================")
 

# food = input(" Enter your today food Name: ").strip()
# eat = "yes" if food == "Cake" else "No"
# print(eat)


age = int(input("Enter your age : "))
vote = ("yes", "No") [age<=18]
print(vote )

print(" ================  00000000 =======================")

salary = int(input("Enter your Salary : "))
taxes = salary*(.01, 0.2) [salary > 5000]
print(taxes)
