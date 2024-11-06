# Check if a year input by the user is a century year.
num =int(input("enter your year:"))

if (num % 100 == 0):
    print("century year")
else:
    print("not a century year")     
    
        