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
class Circle:  
    def __init__(self, radius):  
        self.radius = radius  
    
    def area(self):  
        # circle area  
        return 3 * self.radius * self.radius  
    
    def perimeter(self):  
        #  circle circumference  
        return 2 * 3 * self.radius  

class Square:  
    def __init__(self, side):  
        self.side = side  
    
    def area(self):  
        return self.side * self.side  
    
    def perimeter(self):  
        return 4 * self.side  

class Triangle:  
    def __init__(self, side1, side2, side3):  
        self.side1 = side1  
        self.side2 = side2  
        self.side3 = side3  
    
    def perimeter(self):  
        return self.side1 + self.side2 + self.side3  
    
    def area(self):  
        #  area calculation  
        return 0.5 * self.side1 * self.side2  

# Let's test shapes  
def main():  
    # Create and calculate for different shapes  
    circle = Circle(5)  
    print(f"Circle Area: {circle.area()}")  
    print(f"Circle Perimeter: {circle.perimeter()}")  
    
    square = Square(4)  
    print(f"Square Area: {square.area()}")  
    print(f"Square Perimeter: {square.perimeter()}")  
    
    triangle = Triangle(3, 4, 5)  
    print(f"Triangle Area: {triangle.area()}")  
    print(f"Triangle Perimeter: {triangle.perimeter()}")  

# Run the program  
if __name__ == "__main__":  
    main()   
## 5. Binary Search Tree Class
Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.

# Binary Search Tree Implementation for Beginners

class Node:
    def __init__(self, value):
        self.value = value  # The data in this node
        self.left = None    # Left child starts as None
        self.right = None   # Right child starts as None

class BinarySearchTree:
    def __init__(self):
        self.root = None  # Tree starts empty
    
    def insert(self, value):
        # If tree is empty, create root
        if self.root is None:
            self.root = Node(value)
            return
        
        # Start at the root
        current = self.root
        
        while True:
            # If value is less than current node, go left
            if value < current.value:
                # If left child is empty, insert here
                if current.left is None:
                    current.left = Node(value)
                    break
                # Move to left child
                current = current.left
            
            # If value is greater than or equal to current node, go right
            else:
                # If right child is empty, insert here
                if current.right is None:
                    current.right = Node(value)
                    break
                # Move to right child
                current = current.right
    
    def search(self, value):
        # Start at the root
        current = self.root
        
        # Keep searching while we have a node to check
        while current is not None:
            # If we found the value, return True
            if current.value == value:
                return True
            
            # If value is less, go left
            if value < current.value:
                current = current.left
            
            # If value is greater, go right
            else:
                current = current.right
        
        # If we get here, value wasn't found
        return False
    
    # Bonus: Print tree (in-order traversal)
    def print_tree(self):
        def in_order(node):
            if node:
                # First visit left subtree
                in_order(node.left)
                # Then print current node
                print(node.value, end=" ")
                # Then visit right subtree
                in_order(node.right)
        
        in_order(self.root)
        print()  # New line after printing

# Let's test our Binary Search Tree
def main():
    # Create a new binary search tree
    bst = BinarySearchTree()
    
    # Insert some numbers
    numbers = [5, 3, 7, 1, 4, 6, 8]
    for num in numbers:
        bst.insert(num)
    
    # Print the tree (in-order traversal)
    print("Tree contents:")
    bst.print_tree()
    
    # Search for some values
    print("\nSearching for values:")
    print("Is 4 in the tree?", bst.search(4))   # Should be True
    print("Is 10 in the tree?", bst.search(10)) # Should be False

# Run the program
if __name__ == "__main__":
    main()

    
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

