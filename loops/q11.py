# Print the reverse of a given number.
num=int(input("enter num:"))

reverse =0
while num!=0:
    last_digit =num % 10
    reverse = reverse * 10 + last_digit
    num = num // 10
    
    print("reversed number:" , reverse)