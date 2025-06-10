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

class Stack:
    def __init__(self):
        # Create an empty list to store stack elements
        self.items = []
    
    def push(self, item):
        # Add item to the top of the stack
        self.items.append(item)
    
    def pop(self):
        # Remove and return the top item from the stack
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None
    
    def peek(self):
        # Return the top item without removing it
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None
    
    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0
    
    def size(self):
        # Return the number of items in the stack
        return len(self.items)

def main():
    # Create a new stack
    stack = Stack()
    
    # Demonstrate stack operations
    print("Pushing items:")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    print("Stack size:", stack.size())
    
    print("\nTop item:", stack.peek())
    
    print("\nPopping items:")
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    
    print("\nRemaining stack size:", stack.size())
    
    print("\nIs stack empty?", stack.is_empty())

if __name__ == "__main__":
    main()



## 7. Linked List Data Structure
Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        # Create a new node
        new_node = Node(data)
        
        # If list is empty, make this the head
        if self.head is None:
            self.head = new_node
            return
        
        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next
        
        # Add new node at the end
        current.next = new_node
    
    def delete_node(self, key):
        # If list is empty
        if self.head is None:
            return
        
        # If head node is the one to be deleted
        if self.head.data == key:
            self.head = self.head.next
            return
        
        # Search for the node to delete
        current = self.head
        while current.next:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next
    
    def display(self):
        # If list is empty
        if self.head is None:
            print("List is empty")
            return
        
        # Traverse and print each node
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def main():
    # Create a new linked list
    linked_list = LinkedList()
    
    # Insert some elements
    print("Inserting elements:")
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    
    # Display the list
    print("\nOriginal List:")
    linked_list.display()
    
    # Delete a node
    print("\nDeleting node with value 20:")
    linked_list.delete_node(20)
    
    # Display updated list
    print("Updated List:")
    linked_list.display()

if __name__ == "__main__":
    main()
 
## 8. Shopping Cart Class
Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    def __init__(self):
        # Dictionary to store items and their prices
        self.items = {}
    
    def add_item(self, name, price, quantity=1):
        # Add item to the cart or update quantity
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {'price': price, 'quantity': quantity}
    
    def remove_item(self, name, quantity=1):
        # Remove item from the cart
        if name in self.items:
            if self.items[name]['quantity'] <= quantity:
                # If removing all or more than available, delete the item
                del self.items[name]
            else:
                # Reduce the quantity
                self.items[name]['quantity'] -= quantity
        else:
            print(f"{name} not in cart")
    
    def calculate_total(self):
        # Calculate total price of all items
        return sum(item['price'] * item['quantity'] for item in self.items.values())
    
    def display_cart(self):
        # Show all items in the cart
        if not self.items:
            print("Cart is empty")
            return
        
        print("Shopping Cart:")
        for name, details in self.items.items():
            print(f"{name}: ${details['price']} x {details['quantity']} = ${details['price'] * details['quantity']}")

def main():
    # Create a new shopping cart
    cart = ShoppingCart()
    
    # Add items to the cart
    print("Adding items:")
    cart.add_item("Laptop", 1000, 1)
    cart.add_item("Mouse", 50, 2)
    cart.add_item("Keyboard", 100, 1)
    
    # Display cart contents
    cart.display_cart()
    
    # Calculate and show total
    print(f"\nTotal Price: ${cart.calculate_total():.2f}")
    
    # Remove an item
    print("\nRemoving an item:")
    cart.remove_item("Mouse", 1)
    
    # Display updated cart
    cart.display_cart()
    
    # Show updated total
    print(f"\nUpdated Total Price: ${cart.calculate_total():.2f}")

if __name__ == "__main__":
    main()

    
## 9. Stack with Display
Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.
class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.items = []
    
    def push(self, item):
        # Add item to the top of the stack
        self.items.append(item)
    
    def pop(self):
        # Remove and return the top item from the stack
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None
    
    def display(self):
        # Show all elements in the stack
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack elements (bottom to top):")
            for item in self.items:
                print(item, end=" ")
            print()  # New line after displaying
    
    def peek(self):
        # Return the top item without removing it
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None
    
    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0
    
    def size(self):
        # Return the number of items in the stack
        return len(self.items)

def main():
    # Create a new stack
    stack = Stack()
    
    # Demonstrate stack operations
    print("Pushing items:")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    # Display current stack
    print("\nCurrent Stack:")
    stack.display()
    
    # Peek at top item
    print("\nTop item:", stack.peek())
    
    # Pop an item
    print("\nPopping an item:")
    popped = stack.pop()
    print("Popped item:", popped)
    
    # Display updated stack
    print("\nUpdated Stack:")
    stack.display()
    
    # Check stack size
    print("\nStack size:", stack.size())

if __name__ == "__main__":
    main()

## 10. Queue Data Structure
Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.
class Queue:
    def __init__(self):
        # Initialize an empty list to store queue elements
        self.items = []
    
    def enqueue(self, item):
        # Add item to the end of the queue
        self.items.append(item)
    
    def dequeue(self):
        # Remove and return the first item from the queue
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")
            return None
    
    def is_empty(self):
        # Check if the queue is empty
        return len(self.items) == 0
    
    def size(self):
        # Return the number of items in the queue
        return len(self.items)
    
    def display(self):
        # Show all elements in the queue
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements (front to back):")
            for item in self.items:
                print(item, end=" ")
            print()  # New line after displaying

def main():
    # Create a new queue
    queue = Queue()
    
    # Demonstrate queue operations
    print("Enqueueing items:")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    
    # Display current queue
    print("\nCurrent Queue:")
    queue.display()
    
    # Dequeue an item
    print("\nDequeueing an item:")
    dequeued = queue.dequeue()
    print("Dequeued item:", dequeued)
    
    # Display updated queue
    print("\nUpdated Queue:")
    queue.display()
    
    # Check queue size
    print("\nQueue size:", queue.size())

if __name__ == "__main__":
    main()

## 11. Bank Class
Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        # Initialize bank account details
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        # Add money to the account
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}")
            return True
        else:
            print("Invalid deposit amount")
            return False
    
    def withdraw(self, amount):
        # Remove money from the account
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
            return True
        else:
            print("Insufficient funds or invalid withdrawal amount")
            return False
    
    def get_balance(self):
        # Check current account balance
        return self.balance

class Bank:
    def __init__(self, name):
        # Initialize bank with a name and empty account dictionary
        self.name = name
        self.accounts = {}
    
    def create_account(self, account_number, account_holder, initial_balance=0):
        # Create a new bank account
        if account_number not in self.accounts:
            account = BankAccount(account_number, account_holder, initial_balance)
            self.accounts[account_number] = account
            print(f"Account created for {account_holder}")
            return account
        else:
            print("Account number already exists")
            return None
    
    def find_account(self, account_number):
        # Find and return an account by its number
        return self.accounts.get(account_number)
    
    def transfer_funds(self, from_account, to_account, amount):
        # Transfer funds between accounts
        if from_account in self.accounts and to_account in self.accounts:
            sender = self.accounts[from_account]
            receiver = self.accounts[to_account]
            
            if sender.withdraw(amount):
                receiver.deposit(amount)
                print(f"Transferred ${amount:.2f} from {from_account} to {to_account}")
                return True
        
        print("Transfer failed")
        return False

def main():
    # Create a new bank
    my_bank = Bank("Python Bank")
    
    # Create some accounts
    print("Creating Accounts:")
    account1 = my_bank.create_account("1001", "Alice Johnson", 1000)
    account2 = my_bank.create_account("1002", "Bob Smith", 500)
    
    # Demonstrate account operations
    print("\nAccount Operations:")
    # Deposit
    account1.deposit(200)
    
    # Withdraw
    account1.withdraw(100)
    
    # Check balances
    print(f"\nAlice's Balance: ${account1.get_balance():.2f}")
    print(f"Bob's Balance: ${account2.get_balance():.2f}")
    
    # Transfer funds
    print("\nTransferring Funds:")
    my_bank.transfer_funds("1001", "1002", 300)
    
    # Final balances
    print("\nFinal Balances:")
    print(f"Alice's Balance: ${account1.get_balance():.2f}")
    print(f"Bob's Balance: ${account2.get_balance():.2f}")

if __name__ == "__main__":
    main()


