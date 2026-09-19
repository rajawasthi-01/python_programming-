num = int(input("Enter a number: "))

if num < 0:
    print("sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")    
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print("The factorial of", num, "is", factorial)
       