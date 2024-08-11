def is_even(num):
    return num % 2 == 0

number = int(input("Enter A Number: "))

if is_even(number):
    print(number, "is even.")
else:
    print(number, "is odd.")