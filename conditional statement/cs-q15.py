# Write a program to check if a number is within a specified range.
def check_number_in_range(number, start, end):
    if start <= number <= end:
        return f"The number {number} is within the range of {start} and {end}."
    else:
        return f"The number {number} is NOT within the range of {start} and {end}."
number = float(input("Enter a number: "))
start = float(input("Enter the start of the range: "))
end = float(input("Enter the end of the range: "))
result = check_number_in_range(number, start, end)
print(result)

          
