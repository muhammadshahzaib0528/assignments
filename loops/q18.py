# Use a loop to print numbers in reverse order within a given range.
def print_reverse(start, end):

    for number in range(end, start - 1, -1):
        print(number)
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
print_reverse(start, end)
