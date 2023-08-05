# 1. **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
#     - *Input*: [("John", 25), ("Jane", 30)]
#     - *Output*: "John is 25 years old. Jane is 30 years old."


def print_names_and_ages(data):
    for name, age in data:
        print(f"{name} is {age} years old.")

# Input data as a list of tuples
data = [("John", 25), ("Jane", 30)]

# Call the function to print names and ages
print_names_and_ages(data)






# 1. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"



def add_name_age(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, age):
    if name in dictionary:
        dictionary[name] = age
    else:
        print(f"{name} does not exist in the dictionary.")

def delete_name(dictionary, name):
    if name in dictionary:
        del dictionary[name]
    else:
        print(f"{name} does not exist in the dictionary.")

# Create an empty dictionary
name_age_dict = {}

# Add "John": 25
add_name_age(name_age_dict, "John", 25)
print(name_age_dict)

# Update "John": 26
update_age(name_age_dict, "John", 26)
print(name_age_dict)

# Delete "John"
delete_name(name_age_dict, "John")
print(name_age_dict)



# 1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"


def find_two_sum(nums, target):
    num_dict = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i

    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = find_two_sum(nums, target)
print(result)  # Output: [0, 1] (because nums[0] + nums[1] = 2 + 7 = 9)



# 1. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."



def is_palindrome(s):
    # Remove all non-alphanumeric characters and convert the string to lowercase
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())

    # Compare the cleaned string with its reverse
    return cleaned_s == cleaned_s[::-1]

# Example usage:
string1 = "Able was I, ere I saw Elba."
string2 = "racecar"
string3 = "hello world"

print(is_palindrome(string1))  # Output: True
print(is_palindrome(string2))  # Output: True
print(is_palindrome(string3))  # Output: False




# 1. **Selection Sort**: Implement the selection sort algorithm in Python.
#     - *Input*: [64, 25, 12, 22, 11]
#     - *Output*: "[11, 12, 22, 25, 64]"

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)

# Output: Sorted array: [11, 12, 22, 25, 64]

# 1. **Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"

from queue import LifoQueue

class Stack:
    def __init__(self):
        self.stack = LifoQueue()

    def push(self, item):
        self.stack.put(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.get()

    def is_empty(self):
        return self.stack.empty()

# Example usage:
stack = Stack()

stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2

stack.push(3)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 1



# 1. **FizzBuzz**: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".
#     - *Input*: None
#     - *Output*: "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 
# 16,..."




def fizzBuzz(num):
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Example usage:
fizzBuzz(15)






# 1. **File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
#     - *Input*: A text file named "input.txt" with the content "Hello world"
#     - *Output*: A text file named "output.txt" with the content "Number of words: 2"




def count_words(input_file, output_file):
    try:
        # Read the input file and count the number of words
        with open(input_file, 'r') as file:
            content = file.read()
            word_count = len(content.split())

        # Write the word count to the output file
        with open(output_file, 'w') as file:
            file.write(f"Number of words: {word_count}")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")

# Example usage:
input_file_name = "input.txt"
output_file_name = "output.txt"

count_words(input_file_name, output_file_name)






# 2. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."


def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

# Example usage:
num1 = 5
num2 = 0

output = divide_numbers(num1, num2)
print(output)  # Output: "Cannot divide by zero."


