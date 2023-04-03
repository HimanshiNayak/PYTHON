# factorial of 5
def factorial(n):
    # base case: if n is 1, return 1
    if n == 1:
        return 1
    # recursive case: return n multiplied by the factorial of n-1
    else:
        return n * factorial(n-1)

# example usage
print(factorial(5)) # prints 120
                     
                    # OR 

# Python code to demonstrate naive method
# to compute factorial
n = 23
fact = 1
 
for i in range(1, n+1):
    fact = fact * i
 
print("The factorial of 23 is : ", end="")
print(fact)
