print(" ================  this 1st for loop =======================")

for i in range (5):
    print(i)

print(" ================  this 2nd for loop =======================")


for i in range (5,20):
    print(i)

print(" ================  this  3rd for loop =======================")

for i in range (-8,0): 
    print(i)

print(" ================  this  4th for loop =======================")


frutisList = ["Apple", "Banana", "Mango", "Orange","lemon"]
for frut in frutisList:
  print(frut)

print(" ================  this  5th for loop =======================")

for index, frut in enumerate(frutisList):
    print(f"{index} = ",frut)
 
print(" ================  this  6th for loop =======================")
name = "Injamam Ul Hoque Sifat"

for l in name:
    print(l)