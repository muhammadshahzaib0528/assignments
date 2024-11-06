# Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.
a= float(input("enter 1st number"))
b= float(input("enter 2nd number"))
operator = input("enter an operator (+,-,*,/):")

if operator == "+":   
    print("result:", a + b) 
elif operator == "-":     
    print("result:", a - b)  
elif operator == "*":      
     print("result:", a * b)    
elif (operator == "/"):    
   if b != 0:    
    print("result:", a / b)   
else:
     print("ERROR:division by zero is not allowed")
     print("ERROR: invalid operator.")    
    