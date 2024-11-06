# Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).
a =int(input("angle1:"))
b =int(input("angle2:"))
c =int(input("angle3:"))  

if a == b and b == c:
      print("equilateral")
      
elif a == b and c != a and b:
      print("isosceles") 
elif a!=b  and b!=c:
      print("isosceles") 
      
else:
      print("scalene")       
      