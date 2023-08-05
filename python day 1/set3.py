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
