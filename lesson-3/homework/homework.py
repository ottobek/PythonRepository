# Homework: List and Tuple Exercises

## 1. Create and Access List Elements
Create a list containing five different fruits and print the third fruit.
  
fruits = ["apple", "orange", "plums", "grapes", "banana"]
print(fruits[2]) 

## 2. Concatenate Two Lists
Create two lists of numbers and concatenate them into a single list.

## method 1: 

list_of_furniture = ["sofa", "desk", "cabinet"]
list_of_garden_tools = ["bucket", "saw", "garden fork"]
joined_list = list_of_furniture + list_of_garden_tools
print(joined_list) 

## method 2: 

list1_of_names = ["Lola", "Anora", "Sherzod"]
list2_of_names = ["Lobar", "Zebo", "Komil"]
list1_of_names.extend (list2_of_names) 
print(list1_of_names) 

## 3. Extract Elements from a List
Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

## did dynamically 
numbers = [8, 10, 22, 85, 64]  
new_numbers_list = [  
    numbers[0],           # First element (8)  
    numbers[len(numbers)//2],  # Middle element (22)  
    numbers[-1]           # Last element (64)  
]  
print(new_numbers_list)  # This will print: [8, 22, 64]  

## 4. Convert List to Tuple
Create a list of your five favorite movies and convert it into a tuple.

favorite_movies = ["Breaking Bad", "The Matrix", "Abdullajon", "Temir xotin", "Toy Story"]

# Converting the list to a tuple
movie_tuple = tuple(favorite_movies)

print(favorite_movies)  # Original list
print(movie_tuple)      # New tuple

## 5. Check Element in a List
Given a list of cities, check if "Paris" is in the list and print the result.

  #List of 5 cities
cities = ["Tashkent", "Samarkand", "Bukhara", "Khiva", "Andijan"]
  # Checking if "Paris" is in the list
print("Is Paris in the list?", "Paris" in cities)

  #OR

  cities = ["Tashkent", "Samarkand", "Bukhara", "Khiva", "Andijan"]  
print("Paris" in cities) 
  
## 6. Duplicate a List Without Using Loops
Create a list of numbers and duplicate it without using loops.

original_list = ["Eshmat", "Toshmat", "Ali", "Vali"]  
duplicated_list = original_list[:]
print(duplicated_list)

## 7. Swap First and Last Elements of a List
Given a list of numbers, swap the first and last elements.
a = [10, 20, 30, 40, 50]

# Swapping elements at index 0 and 4
# using multiple assignment
a[0], a[4] = a[4], a[0]

print(a)
## 8. Slice a Tuple
Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  
print(numbers[3:8])    # (4, 5, 6, 7)  

  

## 9. Count Occurrences in a List
Create a list of colors and count how many times "blue" appears in the list.

colors = ["blue", "red", "green", "brown", "blue"]  
blue_count = colors.count("blue")  
print(blue_count) 

  

## 10. Find the Index of an Element in a Tuple
Given a tuple of animals, find the index of "lion".

animals = ("dog", "cat", "elephant", "lion", "tiger")  
lion_index = animals.index("lion")  
print(lion_index)  


## 11. Merge Two Tuples
Create two tuples of numbers and merge them into a single tuple.

tuple1 = (1, 2, 3)  
tuple2 = (4, 5, 6)  
merged_tuple = tuple1 + tuple2  
print(merged_tuple)
  

## 12. Find the Length of a List and Tuple
Given a list and a tuple, find and print their lengths.

my_list = [1, 2, 3, 4, 5]  
my_tuple = (10, 20, 30, 40, 50)  

print(len(my_list))   #list
print(len(my_tuple))  #tuple 
  
## 13. Convert Tuple to List
Create a tuple of five numbers and convert it into a list.

my_tuple = (1, 2, 3, 4, 5)  
my_list = list(my_tuple)  
print(my_list)


## 14. Find Maximum and Minimum in a Tuple
Given a tuple of numbers, find and print the maximum and minimum values.

my_tuple = (5, 2, 9, 1, 7, 3)  

#finding maximum value  
max_value = max(my_tuple)  
#finding minimum value  
min_value = min(my_tuple)  

print("Maximum value:", max_value)   
print("Minimum value:", min_value) 

## 15. Reverse a Tuple
Create a tuple of words and print it in reverse order.

words_tuple = ("dushanba", "seshanba", "juma", "shanba")  

# Reverse the tuple using slice with negative step  
reversed_tuple = words_tuple[::-1]  

print(reversed_tuple)   
