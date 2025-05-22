# Homework Exercises

## 1. Age Calculator
Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

name = input("Ismingizni kiriting: ")
birth_year = int(input("Tug'ilgan yilingizni kiriting: "))
age = 2025 - birth_year 
print(f"Salom {name}, siz {age} yoshdasiz, do'stim.") 


## 2. Extract Car Names
Extract car names from the following text:
```python
txt = 'LMaasleitbtui'
```

txt = 'LMaasleitbtui'
car_name = txt[1] + txt[2] + txt[5] + txt[7] + txt[9] + txt[11]
print(car_name)  # This will print 'Malibu'

## 3. Extract Car Names
Extract car names from the following text:
```python
txt = 'MsaatmiazD'
```

txt = 'Msaatmiazd'
car_name = txt[0] + txt[3] + txt[8] + txt[9] + txt[2]
print(car_name)  # This will print 'Mazda'


## 4. Extract Residence Area
## Extract the residence area from the following text:
txt = "I am John. I am from London"
area = txt.split("from ")[-1]
print(area)  # Should print 'London'  

## 5. Reverse String
Write a Python program that takes a user input string and prints it in reverse order.

user_string = input("Enter a string to reverse: ")
reversed_string = user_string[::-1]
print(reversed_string)

## 6. Count Vowels
Write a Python program that counts the number of vowels in a given string.

text = input("Enter a string to count vowels: ")
vowels = 'aeiouAEIOU'
vowel_count = sum(1 for char in text if char in vowels)
print(f"Number of vowels: {vowel_count}") 

## 7. Find Maximum Value
Write a Python program that takes a list of numbers as input and prints the maximum value.

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
max_value = max(numbers)
print(f"Maximum value: {max_value}")

## 8. Check Palindrome
Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

word = input("Palindrom ekanligini tekshirish uchun so'z kiriting: ")
is_palindrome = word.lower() == word.lower()[::-1]
print("Bu palindrom!" if is_palindrome else "Yo'q, palindrom emas.")

## 9. Extract Email Domain
Write a Python program that extracts and prints the domain from an email address provided by the user.

email = input("E-pochtanigizni kiriting: ")
domain = email.split('@')[-1]
print(f"Email domeni: {domain}")

## 10. Generate Random Password
Write a Python program to generate a random password containing letters, digits, and special characters.

  import random
import string

letters = string.ascii_letters
digits = string.digits
special_chars = '!@#$%^&*'

all_chars = letters + digits + special_chars

# 12-belgili random parol yaratish
password = ''.join(random.choice(all_chars) for _ in range(12))
print(f"Generated Password: {password}")
