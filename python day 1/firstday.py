# 1. **Hello, World!**: Write a Python program that prints "Hello, World!" to the console.
#     - *Input*: None
#     - *Output*: "Hello, World!"

print("Hello, world")


# 2. **Data Type Play**: Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.
#     - *Input*: None
#     # - *Output*: "Type of variable1: <class 'int'>, value: 10..."


int_pyt=45
fl_pyt=3.14
str_pyt="Hello Python"
bool_pyt=True
list_pyt=[1,2,3,4]
tuple_pyt=(1,2,"hello")
dictionary_pyt={"name":"Rohit","lastname":"Chauhan"}
set_pyt=(1,2,3,4)


print("Type of int_pyt:", type(int_pyt), ", value:", int_pyt)
print("Type of fl_pyt:", type(fl_pyt), ", value:", fl_pyt)
print("Type of bool_pyt:", type(bool_pyt), ", value:", bool_pyt)
print("Type of str_pyt:", type(str_pyt), ", value:", str_pyt)
print("Type of list_pyt:", type(list_pyt), ", value:", list_pyt)
print("Type of tuple_pyt:", type(tuple_pyt), ", value:", tuple_pyt)
print("Type of dictionary_pyt:", type(dictionary_pyt), ", value:", dictionary_pyt)
print("Type of set_pyt:", type(set_pyt), ", value:", set_pyt)



# 3. **List Operations**: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
#     - *Input*: None
#     - *Output*: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]..."


def main():
    # Create a list of numbers from 1 to 10
    my_list = list(range(1, 11))
    print("Original list:", my_list)

    # Add a number to the list
    my_list.append(20)
    print("List after adding 20:", my_list)

    # Remove a number from the list
    my_list.remove(5)
    print("List after removing 5:", my_list)

    # Sort the list
    my_list.sort()
    print("Sorted list:", my_list)

if __name__ == "__main__":
    main()



# 4. **Sum and Average**: Write a Python program that calculates and prints the sum and average of a list of numbers.
#     - *Input*: [10, 20, 30, 40]
#     - *Output*: "Sum: 100, Average: 25.0"    


def sumavg():
    number = [10, 20, 30, 40]
    total_sum = sum(number)
    avg_num = total_sum / len(number)

    print("Sum:", total_sum, "Average:", avg_num)

if __name__ == "__main__":
    sumavg()


# 5. **String Reversal**: Write a Python function that takes a string and returns the string in reverse order.
#     - *Input*: "Python"
#     - *Output*: "nohtyP"

def reverse_string(input_string):
    return input_string[::-1]

# Test the function
input_string = "Python"
output_string = reverse_string(input_string)
print(output_string)


# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"


def count_vowels(input_count):
    vowels = "aeiouAEIOU"
    count = 0

    for char in input_count:
        if char in vowels:
            count += 1

    return count

# Test the function
input_count = "Hello"
num_vowels = count_vowels(input_count)
print("Number of vowels:", num_vowels)

    

# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."    


def is_prime(number):
    if number <= 1:
        return False

    # Check if the number is divisible by any integer from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True

# Test the function
num = 6
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")



# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
number = 5
result = factorial(number)
print(f"Factorial of {number} is {result}.")



# 9. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.
#     - *Input*: 5
#     - *Output*: "[0, 1, 1, 2, 3]"


def fibonacci_sequence(n):
    sequence = [0, 1]

    for i in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence[:n]


# Test the function
n = 5
fib_sequence = fibonacci_sequence(n)
print(f"Fibonacci sequence of {n} numbers: {fib_sequence}")



# 10. **List Comprehension**: Use list comprehension to create a list of the squares of the numbers from 1 to 10.
#     - *Input*: None
#     - *Output*: "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"


squares = [i ** 2 for i in range(1, 11)]

print(squares)
