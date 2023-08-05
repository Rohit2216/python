# ### Problem **1: Print the following pattern**

# Write a program to print the following number pattern using a loop.


def pattern():
    for i in range(1, 6):  # Outer loop for 1 and 2
        for j in range(1, i + 1):  # Inner loop to print numbers from 1 to i (inclusive)
            print(j, end=" ")
        print()  # Move to the next line after each inner loop

pattern()


### Problem **2: Display numbers from a list using loop**

# Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions

# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop


def display():
    numbers = [12, 75, 150, 180, 145, 525, 50]

    for number in numbers:

        if number <= 150 and number % 5 == 0:
            print(number)
        elif number > 150 and number < 500:
            continue
        elif number>=500:
            break

display()


### Problem **3: Append new string in the middle of a given string**

# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.


def append_in_middle(s1, s2):
    # Calculate the middle index of s1
    middle_index = len(s1) // 2

    # Create the new string s3 by inserting s2 at the middle index of s1
    s3 = s1[:middle_index] + s2 + s1[middle_index:]

    return s3

# Example usage:
s1 = "hello"
s2 = "beautiful"
result = append_in_middle(s1, s2)
print(result)



### Problem **4: Arrange string characters such that lowercase letters should come first**

# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.


def rearrange_lowercase_first(s):
    lower_chars = [c for c in s if c.islower()]
    upper_chars = [c for c in s if c.isupper()]
    result = ''.join(lower_chars + upper_chars)
    return result

# Example usage:
input_string = "HelloWorld"
output_string = rearrange_lowercase_first(input_string)
print(output_string)



### Problem **5: Concatenate two lists index-wise**

# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# Use list comprehension to concatenate elements from both lists index-wise
result_list = [x + y for x, y in zip(list1, list2)]

print(result_list)


# Problem 6: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# ​
# Expected output:
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

# Use nested loops to concatenate elements from both lists in the specified order
result_list = [x + y for x in list1 for y in list2]

print(result_list)



# Problem 7: Iterate both lists simultaneously
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
# Given
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x,y in zip(list1,reversed(list2)):
    print(x,y)


### Problem **8: Initialize dictionary with default values**

# In Python, we can initialize the keys with the same values.

# **Given**:

# ```
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# ```

# **Expected output:**    

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

employee_dic={employee:
defaults.copy() for employee in employees}
print(employee_dic)



### Problem **9: Create a dictionary by extracting the keys from a given dictionary**

# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

result_dict={key:sample_dict[key] for key in keys}
print(result_dict)


### Problem **10: Modify the tuple**

# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222


tuple1 = (11, [22, 33], 44, 55)

list_inside_tuple = list(tuple1[1])
list_inside_tuple[0] = 222

modified_tuple = (tuple1[0], tuple(list_inside_tuple), tuple1[2], tuple1[3])

print(modified_tuple)
