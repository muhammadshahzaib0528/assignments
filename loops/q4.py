# Print the multiplication table of a given number


inputNum = int(input("Enter any number: "))

for i in range(1, 11):
    
    print(inputNum, " * ", i, " : ", inputNum * i)
