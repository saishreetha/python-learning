import math

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum = num1 + num2
diff = num1 - num2
product = num1 * num2
divide = num1 / num2

print("Sum:", sum)
print("Difference:", diff)
print("Product:", product)
print("Division:", divide)

print("Floor:", math.floor(num1))
print("Ceil:", math.ceil(num1))
print("Absolute:", abs(num1))
print("Round:", round(num1))
print("Max:", max(num1, num2))
print("Min:", min(num1, num2))
print("Power:", math.pow(num1, num2))

'''
Output:
Enter the first number: 4
Enter the second number: 8
Sum: 12.0
Difference: -4.0
Product: 32.0
Division: 0.5
Floor: 4
Ceil: 4
Absolute: 4.0
Round: 4
Max: 8.0
Min: 4.0
Power: 65536.0

'''