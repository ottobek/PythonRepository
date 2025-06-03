# Homework:

# Object-Oriented Programming (OOP) Exercises

## 1. Circle Class
Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

## 2. Person Class
Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.

from datetime import datetime  

class Person:  
    def __init__(self, name, country, date_of_birth):  
        self.name = name               # Name of the person  
        self.country = country         # Country of the person  
        self.date_of_birth = date_of_birth  # Date of birth in format YYYY-MM-DD  
    
    def calculate_age(self):  
        today = datetime.now()  # Get the current date  
        birth_date = datetime.strptime(self.date_of_birth, '%Y-%m-%d')  # Convert string to date  
        age = today.year - birth_date.year  # Calculate age based on years  
        
        # Check if birthday has occurred this year; if not, subtract one  
        if (today.month, today.day) < (birth_date.month, birth_date.day):  
            age -= 1  
        
        return age  

# Example usage  
person = Person("Ali Valiyev", "O'zbekiston", "1990-05-15")  #  a Person object  
print(f"Name: {person.name}")                   # Print the name  
print(f"Country: {person.country}")              # Print the country  
print(f"Age: {person.calculate_age()}")          # Calculate and print the age 
## 3. Calculator Class
Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

## 4. Shape and Subclasses
Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.

## 5. Binary Search Tree Class
Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.

## 6. Stack Data Structure
Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.

## 7. Linked List Data Structure
Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.

## 8. Shopping Cart Class
Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

## 9. Stack with Display
Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.

## 10. Queue Data Structure
Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

## 11. Bank Class
Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.

