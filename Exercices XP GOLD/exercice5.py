
num1 = int(input("Input the 1st number: "))
num2 = int(input("Input the 2nd number: "))    
num3 = int(input("Input the 3rd number: "))
greatest = num1
if num2 > greatest:
    greatest = num2
if num3 > greatest:
    greatest = num3
print("The greatest number is:", greatest)

