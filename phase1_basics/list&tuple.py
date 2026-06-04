""" 
print(" ================  List =======================")

student = ["Inajamam","Shawon","Sagar","Rasel"]
student[0]= "Sifat"
print(student)
print(student[3])
print(student[:3])
print(student[0:])

print(" ================  00000000 =======================")

student = ["Inajamam",25,90,"Rasel"]
print(student[1:3])

print(" ================  00000000 =======================")
student = [40,25,90,50]
student.append(60)
print(student)
print(student.sort(reverse=True))
print(student)

print(" ================  00000000 =======================")

list = [40,25,90,50]
list.reverse()
print(list)

print(list.insert(20,52))
print(list)

print(list.remove(40))
print(list)
  
 

print(" ================  tuple =======================")

number = (40,25,90,50,50,50)

print(type(number))
print(number)
print(number.index(25))
print(number.count(50))
print(number[3])
print(number[:3])
print(number[0:])
"""


print(" ================  00000000 =======================")
# em
movies = []
mov1 = input("Enter 1st movies: ")
mov2 = input("Enter 2nd movies: ")
mov3 = input("Enter 3rd movies: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

print(" ================  00000000 =======================")

movies = []
movies.append(input("Enter 1st movies: "))
movies.append(input("Enter 1st movies: "))
movies.append(input("Enter 1st movies: "))

print(movies)