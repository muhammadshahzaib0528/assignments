# Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.
num=int(input("enter your number:"))

if num  % 2 == 0  and  num % 3 == 0:
    print("divisible by both 2 & 3")
elif num % 2 == 0:
    print("divisible by 2")
elif num  % 3 == 0: 
    print("divisible by 3") 
else:
    print("not divisible by 2 & 3")
              