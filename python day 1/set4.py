# 1. **Anagram Check**: Write a Python function that checks whether two given words are anagrams.
#     - *Input*: "cinema", "iceman"
#     - *Output*: "True"


def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    char_count = {}
    
    # Count characters in str1
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Subtract characters in str2
    for char in str2:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1

    return True

# Test cases
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False





# 2. **Bubble Sort**: Implement the bubble sort algorithm in Python.
#     - *Input*: [64, 34, 25, 12, 22, 11, 90]
#     - *Output*: "[11, 12, 22, 25, 34, 64, 90]"


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize the sorting process
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)  # Output: Sorted array: [11, 12, 22, 25, 34, 64, 90]







# 3. **Longest Common Prefix**: Given a list of strings, find the longest common prefix.
#     - *Input*: ["flower","flow","flight"]
#     - *Output*: "fl"


def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return prefix
        prefix += char

    return prefix

# Example usage:
strings = ["apple", "apricot", "appetizer", "app"]
print(longest_common_prefix(strings))  # Output: "app"





# 4. **String Permutations**: Write a Python function to calculate all permutations of a given string.
#     - *Input*: "abc"
#     - *Output*: "['abc', 'acb', 'bac', 'bca', 'cab', 'cba']"






# 5. **Implement Queue using Stack**: Use Python's stack data structure to implement a queue.
#     - *Input*: enqueue(1), enqueue(2), dequeue(), enqueue(3), dequeue(), dequeue()
#     - *Output*: "1, None, 3, None, None"







# 6. **Missing Number**: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#     - *Input*: [3, 0, 1]
#     - *Output*: "2"









# 7. **Climbing Stairs**: You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#     - *Input*: 3
#     - *Output*: "3"








# 8. **Invert Binary Tree**: Invert a binary tree (mirroring it).
#     - *Input*: A binary tree
#     - *Output*: Inverted binary tree







# 9. **Power of Two**: Given an integer, write a function to determine if it is a power of two.
#     - *Input*: 16
#     - *Output*: "True"







    
# 10. **Contains Duplicate**: Given an array of integers, find if the array contains any duplicates.
#     - *Input*: [1, 2, 3, 1]
#     - *Output*: "True"









# 11. **Binary Search**: Write a function that implements binary search on a sorted array.
#     - *Input*: [1, 2, 3, 4, 5, 6], target = 4
#     - *Output*: "3"








# 12. **Depth First Search (DFS)**: Implement DFS for a graph in Python.
#     - *Input*: A graph
#     - *Output*: Vertices visited in DFS order









# 13. **Breadth First Search (BFS)**: Implement BFS for a graph in Python.
#     - *Input*: A graph
#     - *Output*: Vertices visited in BFS order









# 14. **Quick Sort**: Implement quick sort in Python.
#     - *Input*: [10, 7, 8, 9, 1, 5]
#     -- 
# - *Output*: "[1, 5, 7, 8, 9, 10]"








# 15. **Single Number**: Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#     - *Input*: [4,1,2,1,2]
#     - *Output*: "4"









# 16. **Palindrome Linked List**: Given a singly linked list, determine if it is a palindrome.
#     - *Input*: [1,2,2,1]
#     - *Output*: "True"








# 17. **Implement Trie (Prefix Tree)**: Implement a trie with insert, search, and startsWith methods.
#     - *Input*: insert("apple"), search("apple"), startsWith("app")
#     - *Output*: "True, True"







# 18. **Maximum Subarray**: Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#     - *Input*: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#     - *Output*: "6"








# 19. **Implement Stack using Linked List**: Use Python's linked list data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"





# 20. **Basic Django Web App**: Create a basic web application using Django that has two routes, one that displays "Hello, World!" and one that displays "Goodbye, World!".
#     - *Input*: Visit "/", Visit "/goodbye"
#     - *Output*: "Hello, World!", "Goodbye, World!"