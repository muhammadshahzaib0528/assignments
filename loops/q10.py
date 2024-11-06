# Use a loop to count the number of digits in an integer.
def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    
    digit_count = 0
    while n > 0:
        n //= 10 
        digit_count += 1  
    
    return digit_count

# Example usage:
number = 1234567
print(f"The number of digits in {number} is {count_digits(number)}.")
