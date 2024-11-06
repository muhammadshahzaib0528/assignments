# write a program that checks if a given year is a leap year.
 
year = int(input("enter a year:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):

       print("it ia a leap year:")    
    
else:
    
       print("it is not leap year:")    
