with open("file_operation/data.txt", "w", encoding="utf-8") as file:
    file.write("আমার নাম Injamam\n")
    file.write("আমি Python শিখছি\n")
    file.write("আমি Python শিখছি\n")
    file.write("আমি Python শিখছি\n")
    file.write("আমি Python শিখছি\n")
    file.write("আমি Python শিখছি\n")
    file.write("আমি Python শিখছি\n")
    file.write("আমি Python শিখছি\n")
    file.write("আমি Python শিখছি\n")
    

with open("file_operation/marks.txt", "w", encoding="utf-8") as file:
    n = int(input("কতজন student? "))
    for i in range(n):
        name = input("নাম: ")
        mark = input("নম্বর: ")
        file.write(f"{name} = {mark}\n")

with open("file_operation/marks.txt", "r", encoding="utf-8") as file:
    for line in file:
        if "Karim" in line:
            print(line)



with open("file_operation/data.txt", "a", encoding="utf-8") as file:
    file.write("আমি Flutter developer\n")
    file.write("আমি Dhaka তে থাকি\n")





with open("file_operation/sifat.txt", "w", encoding="utf-8") as file:
    file.write("sifat = 95\n")
    file.write("sagar = 88\n")

import os
os.remove("file_operation/sifat.txt")
print("File Deleted")





# ============================ (close,  readline , readlines, readable ) =============
#  close() — File বন্ধ করা 
file = open("file_operation/data.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()  #  শেষে বন্ধ করো

# # readline() — এক লাইন পড়া
# with open("file_operation/data.txt", "r", encoding="utf-8") as file:
#     line1 = file.readline()  # শুধু প্রথম লাইন
#     line2 = file.readline()  # শুধু দ্বিতীয় লাইন
#     print(line1)
#     print(line2)



#  readlines() — সব লাইন list এ 
# with open("file_operation/data.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()  # সব লাইন list এ আসবে
#     print(lines)

#  readable() — পড়া যাবে কিনা check
# with open("file_operation/data.txt", "r", encoding="utf-8") as file:
#     print(file.readable())  # True

# with open("file_operation/data.txt", "w", encoding="utf-8") as file:
#     print(file.readable())  # False (write mode এ পড়া যায় না)
