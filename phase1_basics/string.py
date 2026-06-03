
str1 = "Injamam Ul Hoque Sifat"

print("==================== 000000000000000000000 ================= ")

print(len(str1))

print(str1)

# python slicing indexing ==================
print("==================== 000000000000000000000 ================= ")
# positive indexing ================================
print(str1[4])
print(str1[:4])
print(str1[4:])
print(str1[1:4])
print(str1[::])
print(str1[1:])
print(str1[:25])


print("==================== 000000000000000000000 ================= ")

# negative Indexing ===========
print(str1[-4:])
print(str1[-4:-1])
print(str1[::])
print(str1[-1:])
print(str1[:-10])


print("==================== String Functions  ================= ")

print(str1.endswith("si"))
print(str1.capitalize())
print(str1.replace("a","o"))
print(str1.find("a"))
print(str1.find("Sifat"))
print(str1.count("a"))