#  ============== page 32 and program No : 03 ================
#Program to calculate the product of numbers using the function:
# def multiply(numbers):
#     total = 1
#     for x in numbers: 
#         total *= x 
#     return total
# print(" this is my total muliplication answer: ",multiply([8,6,9,10,7]))

#  =============== 00000000000000000000000 ========================== 

#  ============== page 32 and program No : 04 ================

# Program to find the factorial value of a number using the function:


# def factorial(n):
#     if n == 0 :
#         return 1
#     else:
#         return n*factorial(n-1)
# n = int(input("Input a number : "))
# print(factorial(n))



#  =============== 00000000000000000000000 ========================== 

#  ============== page 32 and program No : 05 ================

# Program to determine if a struggle is fundamental using functions

def test_prime(n):
    if (n==1):
        return False
    elif(n==2):
        return True
    else:
        for x in range(2,n):
            if(n%x==0):
                return False
        return True
print(test_prime(int(input("Input Number: "))))

