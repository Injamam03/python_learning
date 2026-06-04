print(" ================  00000000 =======================")
# this dictionary =======================
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