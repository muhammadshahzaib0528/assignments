# Print the sum of even and odd numbers separately up to a given number.
def sum_even_odd(n):
    sum_even = 0
    sum_odd = 0
    
    for i in range(1, n + 1):  
        if i % 2 == 0:  
            sum_even += i
        else:
            sum_odd += i
    
    # Print the results
    print("Sum of even numbers:", sum_even)
    print("Sum of odd numbers:", sum_odd)

n = 10
sum_even_odd(n)
