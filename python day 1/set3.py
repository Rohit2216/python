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
