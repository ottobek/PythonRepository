# Homeworks

## 1. Modify String with Underscores
Given a string `txt`, insert an underscore (`_`) after every third character. If a character is a vowel or already has an underscore after it, shift the underscore placement to the next character. No underscore should be added at the end.

### Examples
**Input:** `hello`
**Output:** `hel_lo`

**Input:** `assalom`
**Output:** `ass_alom`

**Input:** `abcabcabcdeabcdefabcdefg`
**Output:** `abc_abcab_cdeabcd_efabcdef_g`

def insert_underscores(txt):
    result = []
    count = 0
    i = 0
    vowels = 'aeiou'

    while i < len(txt):
        result.append(txt[i])
        count += 1

        if count == 3:
                     if txt[i] in vowels or (i + 1 < len(txt) and txt[i + 1] == '_'):
                if i + 1 < len(txt) and txt[i + 1] != '_':
                    result.append(txt[i + 1])
                    i += 1
            if i + 1 < len(txt):  # Oxiriga qo‘shilmasligi kerak
                result.append('_')
            count = 0
        i += 1

    # Agar oxirgi belgi '_' bo‘lsa, olib tashlaymiz
    if result and result[-1] == '_':
        result.pop()

    return ''.join(result)


print(insert_underscores("hello"))          # hel_lo
print(insert_underscores("assalom"))        # ass_alom
print(insert_underscores("abcabcabcdeabcdefabcdefg"))  
# abc_abcab_cdeabcd_efabcdef_g


---

## 2. Integer Squares Exercise

### Task
The provided code stub reads an integer, `n`, from STDIN. For all non-negative integers `i` where `0 <= i < n`, print `i^2`.

### Example Input
```
5
```

### Example Output
```
0
1
4
9
16
```

### Input Format
The first and only line contains the integer, `n`.

### Constraints
- `1 <= n <= 20`

### Output Format
Print `n` lines, one corresponding to each `i^2` where `0 <= i < n`.


def squares_generator(n):
    """
    Generate and print squares of numbers from 0 to n-1
    
    Args:
    n (int): Upper limit of numbers to square
    """
    # Loop through numbers from 0 to n-1
    for i in range(n):
        # Calculate and print the square of each number
        print(i ** 2)

# Input method to match the problem description
def main():
    # Read the input number
    n = int(input().strip())
    
    # Call the function to generate squares
    squares_generator(n)

# Uncomment the line below to run with manual input
# main()

# Test cases
print("Test case 1:")
squares_generator(5)

print("\nTest case 2:")
squares_generator(3)

---

## 3. Loop-Based Exercises

### Exercise 1: Print first 10 natural numbers using a while loop

count = 1
while count <= 10:
    print(count)
       count = count + 1 

### Exercise 2: Print the following pattern
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

### Exercise 3: Calculate sum of all numbers from 1 to a given number
**Example:**
```
Enter number 10
Sum is: 55
```
number = int(input("Enter number: "))
total = sum(range(1, number + 1))
print("Sum is:", total)

### Exercise 4: Print multiplication table of a given number
**Example:**
```
2
4
6
8
10
12
14
16
18
20
```

num = int(input("Enter a number: "))  
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")  
### Exercise 5: Display numbers from a list using a loop
**Given:**
```python
numbers = [12, 75, 150, 180, 145, 525, 50]
```

numbers = [12, 75, 150, 180, 145, 525, 50]
for number in numbers:
    if number > 150:
        continue
    if number > 70:
        print(number) 

        
**Expected Output:**
```
75
150
145
```

### Exercise 6: Count the total number of digits in a number
**Example:**
```
75869
Output: 5
```

number = input()
print("Output:", len(number))

### Exercise 7: Print reverse number pattern
```
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
```

n = 5
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

### Exercise 8: Print list in reverse order using a loop
**Given:**
```python
list1 = [10, 20, 30, 40, 50]
```
**Expected Output:**
```
50
40
30
20
10
```

list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)

### Exercise 9: Display numbers from -10 to -1 using a for loop
```
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
```

for i in range(-10, 0):
    print(i)

### Exercise 10: Display message “Done” after successful loop execution
**Example:**
```python
0
1
2
3
4
Done!
```

for i in range(5):
    print(i)
print("Done!")

### Exercise 11: Print all prime numbers within a range
**Example:**
```
Prime numbers between 25 and 50:
29
31
37
41
43
47
```

start, end = 25, 50
print("Prime numbers between", start, "and", end, ":")
for num in range(start, end + 1):
    is_prime = True
    if num < 2:
        is_prime = False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

### Exercise 12: Display Fibonacci series up to 10 terms
**Example:**
```
Fibonacci sequence:
0  1  1  2  3  5  8  13  21  34
```

n_terms = 10  

fib_sequence = [0, 1]  

for i in range(2, n_terms):  
    next_term = fib_sequence[i - 1] + fib_sequence[i - 2]  
    fib_sequence.append(next_term)  

print("Fibonacci sequence:")  
for term in fib_sequence:  
    print(term, end="  ")

### Exercise 13: Find the factorial of a given number
**Example:**
```
5! = 120
```
def factorial(n):  
    result = 1  # Initialize result  
    for i in range(1, n + 1):  
        result *= i  # Multiply result by each number up to n  
    return result  
number = int(input("Enter a number: "))  
fact = factorial(number)  
print(f"{number}! = {fact}")
---

## 4. Return Uncommon Elements of Lists
### Task
Return the elements that are not common between two lists. The order of elements does not matter.

### Examples
- **Input:** `list1 = [1, 1, 2], list2 = [2, 3, 4]`  
  **Output:** `[1, 1, 3, 4]`

- **Input:** `list1 = [1, 2, 3], list2 = [4, 5, 6]`  
  **Output:** `[1, 2, 3, 4, 5, 6]`

- **Input:** `list1 = [1, 1, 2, 3, 4, 2], list2 = [1, 3, 4, 5]`  
  **Output:** `[2, 2, 5]`

  from collections import Counter  

def uncommon_elements(list1, list2):  
    combined = list1 + list2  
    counts = Counter(combined)  
    result = [item for item in counts if counts[item] == 1]  
    return result  

list1_a = [1, 1, 2]  
list2_a = [2, 3, 4]  
output_a = uncommon_elements(list1_a, list2_a)  
print(f"Output: {output_a}")  

list1_b = [1, 2, 3]  
list2_b = [4, 5, 6]  
output_b = uncommon_elements(list1_b, list2_b)  
print(f"Output: {output_b}")  

list1_c = [1, 1, 2, 3, 4, 2]  
list2_c = [1, 3, 4, 5]  
output_c = uncommon_elements(list1_c, list2_c)  
print(f"Output: {output_c}")

