Homeworks:

# Python Dictionary and Set Exercises

## Dictionary Exercises

### 1. Sort a Dictionary by Value
Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 3}  

# Ascending order 
sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))  
print("Sorted (Ascending):", sorted_asc)  

# Descending
sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))  
print("Sorted (Descending):", sorted_desc)  

### 2. Add a Key to a Dictionary
Write a Python script to add a key to a dictionary.
my_dict = {'name': 'Ali', 'age': 22}  
my_dict['city'] = 'Bukhara'  
print("Update:", my_dict)  
**Sample Dictionary:**
```python
{0: 10, 1: 20}
```

**Expected Result:**
```python
{0: 10, 1: 20, 2: 30}
```

# Original dictionary  
sample_dict = {0: 10, 1: 20}  

# Direct assignment   
sample_dict[2] = 30  
print("After adding key:", sample_dict)   


### 3. Concatenate Multiple Dictionaries
Write a Python script to concatenate the following dictionaries to create a new one.

**Sample Dictionaries:**
```python
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
```

**Expected Result:**
```python
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
```
dic1 = {1: 10, 2: 20}  
dic2 = {3: 30, 4: 40}  
dic3 = {5: 50, 6: 60}  

# Combining dictionaries using ** unpacking  
combined_dict = {**dic1, **dic2, **dic3}  
print("Combined Dictionary:", combined_dict)  
             
### 4. Generate a Dictionary with Squares
Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form `(x, x*x)`.

**Sample Dictionary (n = 5):**
```python
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```
### Sorry, I don't get it. 
    
### 5. Dictionary of Squares (1 to 15)
Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

**Expected Output:**
```python
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
```

squares = {}  
for x in range(1, 16):  
    squares[x] = x * x  
print(squares)  

## Set Exercises

### 1. Create a Set
Write a Python program to create a set.

fruits_set = {'nok', 'banan', 'olma'}  
print("Jingalak qavsli set:", fruits_set)  

### 2. Iterate Over a Set
Write a Python program to iterate over sets.

fruits_set = {'nok', 'banan', 'olma'}  
print("mevalar bitta-bitta:")  
for fruit in fruits_set:  
    print(fruit)  

### 3. Add Member(s) to a Set
Write a Python program to add member(s) to a set.

fruits_set = {'nok', 'banan', 'olma'}  
print("Edi:", fruits_set)  

fruits_set.add('handalak')  
print("Qo'shildi:", fruits_set)  

### 4. Remove Item(s) from a Set
Write a Python program to remove item(s) from a given set.

fruits_set.remove('handalak')  
print("remove() bilan o'chirildi:", fruits_set)   

### 5. Remove an Item if Present in the Set
Write a Python program to remove an item from a set if it is present in the set.

fruits_set.discard('banan')  
print("discard() bilan banan o'chirildi:", fruits_set)  

