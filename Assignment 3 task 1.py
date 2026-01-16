def factorial(number):
    if number == 1 or number == 0:
        return 1
    return number * factorial(number-1)

num = int(input("Enter the number: "))
result = factorial(num)
print(f"Factorial of {num} is {result}")




