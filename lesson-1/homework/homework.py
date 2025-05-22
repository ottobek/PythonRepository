Homework:
1. Given a side of square. Find its perimeter and area.

# Getештп the side length from user
side = float(input("Enter the side length of the square: "))

# Calculating perimeter and area
perimeter = 4 * side
area = side ** 2

# Getting the results
print("Perimeter of the square:", perimeter)
print("Area of the square:", area) 

2. Given diameter of circle. Find its length.

diameter = float(input("Enter the diameter of the circle: "))
circumference = 3.14 * diameter
print(f"Circumference of the circle: {circumference}")
  
3. Given two numbers a and b. Find their mean.
# Get two numbers from user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Calculate the mean
mean = (a + b) / 2

# Show the result
print("The mean of", a, "and", b, "is:", mean)
  
4. Given two numbers a and b. Find their sum, product and square of each number.

# Getting two numbers from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Calculates sum, product, and squares
sum_result = a + b
product = a * b
square_a = a ** 2
square_b = b ** 2

# Getting the results
print("Sum:", sum_result)
print("Product:", product)
print("Square of", a, ":", square_a)
print("Square of", b, ":", square_b)
