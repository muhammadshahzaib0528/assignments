# Write a program to find the largest of three numbers.
num1 = int(input("1st num:"))
num2 = int(input("2nd num:"))
num3 = int(input("3rd num:"))

if num1 > num2 and num1 > num3:
 
   print(num1, "is greater than", num2 ,  " and " , num3 )
   
elif num2 > num1 and num2 > num3:
    
    print (num2, "is grater than", num1 ," and " , num3)
       
elif  num3 > num1 and num3 > num2:
    
     print(num3, "is greater than", num1 ,"and", num2)
     
            