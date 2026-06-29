"""
with open("practice_file_operation/test.txt","w") as file:
    file.write("my name is Injamam Ul Hoque Sifat\n")
    file.write("I learn python\n")
    file.write("I learn python\n")
    file.write("I learn python\n")
    file.write("I learn python\n")
    file.write("I learn python\n")
    file.write("I learn python\n")

    file.close

with open("practice_file_operation/testone.txt","w") as file:
    file.write("we are learing python easily")


with open("practice_file_operation/marks.txt","w") as file:
    n = int(input("the number of student: "))
    for i in range(n):
        name = input("name: ")
        mark = input("marks: ")
        file.write(f"{name} = {mark}\n")"""

with open("practice_file_operation/studentinfo.txt","w") as file:
    n=int(input("the number of studen : "))
    department = "Computer"
    for i in range(n):
        print(f"\n ==== student {i+1} ====")
        name = input("name: ")
        roll = input("Roll: ")
        # department = input("Department: ")
        math = input("Math : ")
        python = input("Python : ")

        file.write(f"name : {name}\n")
        file.write(f"Roll : {roll}\n")
        file.write(f"department : {department}\n")
        file.write(f"math : {math}\n")
        file.write(f"python : {python}\n")
        






        




























































"""with open("practice_file_operation/data.txt", "a", encoding="utf-8") as file:
    file.write(" I am a Flutter developer\n")
    file.write("I live in Dhaka\n")"""

"""with open("practice_file_operation/marks.txt", "w", encoding="utf-8") as file:
    n = int(input("how much student? "))
    for i in range(n):
        name = input("name: ")
        mark = input("marks: ")
        file.write(f"{name} = {mark}\n")"""


"""with open("practice_file_operation/marks.txt", "w", encoding="utf-8") as file:
    n = int(input("how much student?"))
    for i in range(n):
        print(f"\n--- Student {i+1} ---")

        name = input("name: ")
        roll = input("roll: ")
        department = input("department: ")
        physics = input("physics: ")
        chemistry = input("chemistry: ")
        
        file.write(f"name : {name}\n")
        file.write(f"roll: {roll}\n")
        file.write(f"department: {department}\n")
        file.write(f"physics : {physics}\n")
        file.write(f"chemistry: {chemistry}\n")
        file.write(f"\n")

print("Save successfully!")"""