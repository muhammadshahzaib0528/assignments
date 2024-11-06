#  Find the factorial of a number using a while loop.


factNum = 5
fac = 1
i = 5
while i >= 1:
    print("fac : ", fac, " i: ", i)
    fac = fac * i
    i = i - 1

print("final factorial of ", factNum, " is ", fac)