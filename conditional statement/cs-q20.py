# Create a program that evaluates if an inputted number is prime.
number = int(input("Enter an integer: "))
          
if number < 2:
    print(number, "is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")