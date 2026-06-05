"""
print(" ================  00000000 =======================")
######### ============ dictionary in python ===============#############
info ={
    "name"    : "Injama",
    "subject" : ["python","c", "java", "dart"],
    "topics"  : ("dic","set"),
    "roll"    : 24,
    "age"     : 23,
    "learning": "Coding",
    "is_adult": "True",
    "marks"   : 5.00
}

info["name"] = "Injamam "

new_info ={"adress": "cox's bazar"}
info.update(new_info)

print(type(info))
print(info)
print(info["name"])
print(info["learning"])
print(info["marks"])

print(" ================  00000000 =======================")
# this is nested dictionary =======================

student = {
    "name": "Sifat",
    "subject" : {
        "math" : 50,
        "phy" : 20,
        "chem" :90

    },
    "roll": 15
}

print(student)
print(student["subject"])
print(student["subject"]["math"])
# use dictionary methods . 
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))
print(list(student.items())[0])
  
print("================= 00000000000000  =======================")
marks = {}


x = int(input("Enter your physics mark : "))
marks.update({"Physisces " :  x})


x = int(input("Enter your english mark : "))
marks.update({"english " :  x})

x = int(input("Enter your math mark : "))
marks.update({"math " :  x})


print(marks)
print(type(marks))








######## ============ set in python ===============#############

collection = {1,8,9,0,}
print(collection)
print(type(collection))

print("================= 00000000000000  =======================")

collection = {1,8,9,0,"math","english","math"}
print(collection)
print(type(collection))


collection = set()  #this is syntax of empty set 

# set methods. (add, remove, clear, pop) . most important sets mutable but element immutable

collection = set()
collection.add("a")
collection.add(1)
collection.add(2)
# collection.remove("a")
# collection.clear()
# collection.pop()
print(collection)

print("================= 00000000000000  =======================")

# extra important se methods (union and intersection)

set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1)
print(set2)


"""




##################################===============   Loops    =================########################################


# count = 1 
# while count <=100:
#     # print("hello")
#     count += 1
#     print(count, "= hello")



# i = 5 
# while i >= 1:
#     print('hellow')
#     i -= 1
# print("loop is end")



# i = 1
# while  i <= 10 :
#     print("3 X ",i, " = ", i*3)
#     i += 1




# n = int(input("Enter your number: "))
# i = 1
# while  i <= 10 :
#     print(n*i)
#     i += 1








a = 34
while a<= 100:
    print(a)
    a += 1;