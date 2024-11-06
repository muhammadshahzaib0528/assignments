# Create a program to calculate the sum of the digits of an inputted integer.

def sum_of_digits(n):
    n = abs(n)

    return sum(int(digit) for digit in str(n))
number = int(input("Enter an integer: "))
print(f"The sum of the digits is: {sum_of_digits(number)}")