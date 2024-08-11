def factorial(num):
    """"Calculates the factiorial of a number.
    
    Args :
        num: The number for which to find the factorial.

    Returns :
        The factorial of the number.
    """


if num == 0 or num == 1:
    return 1
else:
    return num = factorial(num - 1)

number = int(input("Enter a number: "))
result = factorial(number)
print("The factorial of", number, "is:", result)