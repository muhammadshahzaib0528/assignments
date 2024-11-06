# Write a program that breaks the loop when a certain condition is met.

for i in range(1, 10):
    print(i)
    if i == 5:
        print("Condition met: Breaking the loop!")
        break
