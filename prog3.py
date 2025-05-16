def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
    
print(factorial.__doc__)
print("the factorial of 0:",factorial(0))
print("the factorial of 0:",factorial(1))
print("the factorial of 0:",factorial(2))
print("the factorial of 0:",factorial(5))
print("the factorial of 0:",factorial(10))