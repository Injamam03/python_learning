#  ============== page 32 and program No : 03 ================

# def multiply(numbers):
#     total = 1
#     for x in numbers: 
#         total *= x 
#     return total
# print(" this is my total muliplication answer: ",multiply([8,6,9,10,7]))

#  =============== 00000000000000000000000 ========================== 

def factorial(n):
    if n == 0 :
        return 1
    else:
        return n*factorial(n-1)
n = int(input("Input a number : "))
print(factorial(n))