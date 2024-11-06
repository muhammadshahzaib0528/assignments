# Create a program that checks if a given string is a palindrome.
text = str(input("write your number or text:"))


if text == text[::-1]:
    print("this is palindrome.")
    
else:
    print("this is not a palindrome.")    