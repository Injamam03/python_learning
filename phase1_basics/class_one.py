print("====================")

def add_fun(a,b):
    return a+b
print("====================")

import math
def Triangle():
    a = int(input("Enter the value of a:"))
    b = int(input("Enter the value of b:"))
    c = int(input("Enter the value of c:"))
    if (a+b) > c and (b+c) > a and (c+a) > b:
        s = (a + b + c) / 2
        Area = math.sqrt(s * (s-a) * (s-b) * (s-c))
        print("Area of the triangle is:", Area)
    else:
        print("The triangle is not possible")





















"""def multi(numbers):
    total = 1
    for x in numbers:
        total = total * x
    return total      

print(multi((10,20,20.60))) """

"""for i in range(1,50):
    print(f"5 x {i} =",i*5)"""
 


"""def test_prime(n):
    if (n==1):
        return False
    elif(n==2):
        return True
    else:
        for i in range(2,n):
            if(n%i==0):
                return False
        return True
print(test_prime(int(input("Input Number: "))))
"""


"""def fibo (n):
    if n<=1:
        return n
    else:
      return fibo(n-1) + fibo(n-2)
n = int(input("Enter the value of N : "))
print("fibo Serles....:")
for i in range(n):
 print(fibo(i),end=" ")"""



"""import math
def Triangle():
      
    a = int(input("Enter the value of a:"))
    b = int(input("Enter the value of b:"))
    c = int(input("Enter the value of c:"))
    
    if (a+b) > c and (b+c) > a and (c+a) > b:
        s = (a + b + c) / 2
        Area = math.sqrt(s * (s-a) * (s-b) * (s-c))
        print("Area of the triangle is:", Area)
    else:
        print("The triangle is not possible")

Triangle()"""


"""def summation():
    n = 1
    sum = 0
    for n in range(100):
        if n % 2 == 0:
            continue
        sum = sum + n
    return sum

add = summation()
print("The summation is:", add)"""


def summation():
    sum = 0
    for n in range(100):
        if n % 2 == 0:
            sum = sum + n
    return sum

# add = summation()




