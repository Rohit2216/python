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


def permutations_without_repetition(s):
    if len(s) == 0:
        return [""]
    
    all_permutations = []
    for i in range(len(s)):
        first_char = s[i]
        remaining_chars = s[:i] + s[i+1:]
        
        # Recursively find permutations of the remaining characters
        remaining_permutations = permutations_without_repetition(remaining_chars)
        
        # Combine the first character with each permutation of the remaining characters
        for perm in remaining_permutations:
            all_permutations.append(first_char + perm)
    
    return all_permutations

# Example usage:
word = "abc"
result = permutations_without_repetition(word)
print(result)




# 5. **Implement Queue using Stack**: Use Python's stack data structure to implement a queue.
#     - *Input*: enqueue(1), enqueue(2), dequeue(), enqueue(3), dequeue(), dequeue()
#     - *Output*: "1, None, 3, None, None"


class QueueUsingStack:
    def __init__(self):
        self.stack1 = []  # Main stack for enqueueing elements
        self.stack2 = []  # Temporary stack for dequeueing elements

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:  # If stack2 is empty, move elements from stack1
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:  # If both stacks are empty, the queue is empty
            return None
        return self.stack2.pop()

    def is_empty(self):
        return not (self.stack1 or self.stack2)

    def size(self):
        return len(self.stack1) + len(self.stack2)

# Example usage:
queue = QueueUsingStack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2

queue.enqueue(4)
print(queue.dequeue())  # Output: 3
print(queue.dequeue())  # Output: 4

print(queue.is_empty())  # Output: True





# 6. **Missing Number**: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#     - *Input*: [3, 0, 1]
#     - *Output*: "2"



def find_missing_number(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2  # Sum of the first n natural numbers
    actual_sum = sum(nums)       # Sum of the elements in the array

    return total_sum - actual_sum

# Example usage:
nums = [0, 1, 3, 4, 5]
missing_number = find_missing_number(nums)
print("Missing number:", missing_number)  # Output: Missing number: 2






# 7. **Climbing Stairs**: You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#     - *Input*: 3
#     - *Output*: "3"



def climb_stairs(n):
    if n <= 2:
        return n

    # Initialize a list to store the number of ways for each step
    ways = [0] * (n + 1)

    # There is only one way to reach the first two steps (0 and 1 step)
    ways[0], ways[1] = 1, 1

    # Calculate the number of ways for each step up to n
    for i in range(2, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]

# Example usage:
n = 3
distinct_ways = climb_stairs(n)
print("Distinct ways to climb the staircase:", distinct_ways)  # Output: 3





# 8. **Invert Binary Tree**: Invert a binary tree (mirroring it).
#     - *Input*: A binary tree
#     - *Output*: Inverted binary tree



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(root):
    if not root:
        return None

    # Swap left and right subtrees using recursion
    root.left, root.right = invert_binary_tree(root.right), invert_binary_tree(root.left)

    return root

# Example usage:
# Create the original binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Invert the binary tree
inverted_root = invert_binary_tree(root)

# Display the result (in-order traversal for verification)
def in_order_traversal(node):
    if not node:
        return
    in_order_traversal(node.left)
    print(node.val, end=" ")
    in_order_traversal(node.right)

print("Original Binary Tree:")
in_order_traversal(root)  # Output: 4 2 5 1 6 3 7

print("\nInverted Binary Tree:")
in_order_traversal(inverted_root)  # Output: 7 3 6 1 5 2 4






# 9. **Power of Two**: Given an integer, write a function to determine if it is a power of two.
#     - *Input*: 16
#     - *Output*: "True"




def is_power_of_two(n):
    if n <= 0:
        return False

    # Check if only one bit is set (i.e., n & (n - 1) is 0)
    return n & (n - 1) == 0

# Example usage:
print(is_power_of_two(4))  # Output: True (2^2)
print(is_power_of_two(16)) # Output: True (2^4)
print(is_power_of_two(7))  # Output: False



    
# 10. **Contains Duplicate**: Given an array of integers, find if the array contains any duplicates.
#     - *Input*: [1, 2, 3, 1]
#     - *Output*: "True"




def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Example usage:
print(contains_duplicate([1, 2, 3, 4, 5]))     # Output: False (no duplicates)
print(contains_duplicate([1, 2, 3, 4, 1]))     # Output: True (duplicate: 1)
print(contains_duplicate([7, 9, 3, 2, 6, 2]))  # Output: True (duplicate: 2)





# 11. **Binary Search**: Write a function that implements binary search on a sorted array.
#     - *Input*: [1, 2, 3, 4, 5, 6], target = 4
#     - *Output*: "3"



def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found in the array

# Example usage:
arr = [1, 2, 3, 4, 5, 6]
target = 4
index = binary_search(arr, target)
print("Output:", index)  # Output: 3





# 12. **Depth First Search (DFS)**: Implement DFS for a graph in Python.
#     - *Input*: A graph
#     - *Output*: Vertices visited in DFS order




class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, []).append(u)

    def dfs(self, node, visited):
        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            for neighbor in self.graph.get(node, []):
                self.dfs(neighbor, visited)

    def depth_first_search(self, start_node):
        visited = set()
        self.dfs(start_node, visited)
        print()  # Print a newline after DFS traversal

# Example usage:
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(4, 6)

print("Depth-First Search Traversal:")
graph.depth_first_search(1)





# 13. **Breadth First Search (BFS)**: Implement BFS for a graph in Python.
#     - *Input*: A graph
#     - *Output*: Vertices visited in BFS order









# 14. **Quick Sort**: Implement quick sort in Python.
#     - *Input*: [10, 7, 8, 9, 1, 5]
#     -- 
# - *Output*: "[1, 5, 7, 8, 9, 10]"




from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                print(node, end=" ")

                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        print()  # Print a newline after BFS traversal

# Example usage:
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(4, 6)

print("Breadth-First Search Traversal:")
graph.bfs(1)




# 15. **Single Number**: Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#     - *Input*: [4,1,2,1,2]
#     - *Output*: "4"



def find_single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Example usage:
nums = [4, 1, 2, 1, 2]
single_number = find_single_number(nums)
print("Single Number:", single_number)  # Output: 4






# 16. **Palindrome Linked List**: Given a singly linked list, determine if it is a palindrome.
#     - *Input*: [1,2,2,1]
#     - *Output*: "True"



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    # Step 1: Find the middle of the linked list
    def find_middle(head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Step 2: Reverse the second half of the linked list
    def reverse_list(head):
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

    if not head or not head.next:
        return True

    middle = find_middle(head)
    second_half = reverse_list(middle)

    # Step 3: Compare the first and reversed second halves
    while second_half:
        if head.val != second_half.val:
            return False
        head = head.next
        second_half = second_half.next

    return True

# Example usage:
# 1 -> 2 -> 3 -> 2 -> 1 is a palindrome
linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
print(is_palindrome(linked_list))  # Output: True

# 1 -> 2 -> 3 is not a palindrome
linked_list = ListNode(1, ListNode(2, ListNode(3)))
print(is_palindrome(linked_list))  # Output: False







# 17. **Implement Trie (Prefix Tree)**: Implement a trie with insert, search, and startsWith methods.
#     - *Input*: insert("apple"), search("apple"), startsWith("app")
#     - *Output*: "True, True"



class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))     # Output: True
print(trie.startsWith("app"))   # Output: True
print(trie.search("app"))       # Output: False (searching for a full word, "app" is not in the Trie)






# 18. **Maximum Subarray**: Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#     - *Input*: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#     - *Output*: "6"




def max_subarray_sum(nums):
    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = max_subarray_sum(nums)
print("Maximum Subarray Sum:", max_sum)  # Output: 6






# 19. **Implement Stack using Linked List**: Use Python's linked list data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"





# 20. **Basic Django Web App**: Create a basic web application using Django that has two routes, one that displays "Hello, World!" and one that displays "Goodbye, World!".
#     - *Input*: Visit "/", Visit "/goodbye"
#     - *Output*: "Hello, World!", "Goodbye, World!"