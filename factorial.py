'''
n=int(input())
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(n))
factorial(n)
'''
# This code calculates the factorial of a given number n using recursion.
# The function factorial calls itself with decremented values until it reaches the base case
n=int(input("Enter a number: "))
factorial=1
for i in range(1,n+1):
    factorial *= i
print(f"The factorial of {n} is {factorial}")