# Take three sides of a triangle as input and check if they form a valid triangle.

a= int(input("angle1:"))
b= int(input("angle2:")) 
c= int(input("angle3:")) 

if a+b+c ==180:
    print("this is a triangle")
    
else:
    print("not a triangle")