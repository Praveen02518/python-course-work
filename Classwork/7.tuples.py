#1. Introduction to Tuples

#Tuple Creation Syntax:
# Empty Tuple
empty_tuple = ()
# Single-element Tuple (note the trailing comma)
single_tuple = (5,)
# Multi-element Tuple
my_tuple = (1, "apple", 3.5)
# Without parentheses (implicit tuple creation)
implicit_tuple = 1, 2, 3

#2. Accessing Tuple Elements
#a. Indexing
#● Access elements using zero-based indexing.● Syntax: tuple[index]
#● Example:
my_tuple = (10, 20, 30, 40)
print(my_tuple[2]) # Output: 30
#b.Negative Indexing
#● Access elements from the end of the tuple using negative indices.
#● Example:
my_tuple = (10, 20, 30, 40)
print(my_tuple[-1]) # Output: 40

#c. Slicing
#● Extract a portion of the tuple using slicing ([start:end:step]).● Syntax: tuple[start:end]
#● Example:
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[1:4]) # Output: (20, 30, 40) 

#3.Operations on Tuples
#a. Concatenation
#● Combine two or more tuples using the + operator.
#● Example:
tuple1 = (1, 2)
tuple2 = (3, 4)
new_tuple = tuple1 + tuple2 # Output: (1, 2, 3, 4)

#b. Repetition
#● Repeat the elements of a tuple using the * operator.
#● Example:
my_tuple = (1, 2)
print(my_tuple * 3) # Output: (1, 2, 1, 2, 1, 2)

#c. Membership Testing
#● Check if an element is present in the tuple using the in or not in keywords.
#● Example:
my_tuple = (1, 2, 3)
print(2 in my_tuple) # Output: True
print(5 not in my_tuple) # Output: True

#d. Tuple Unpacking
#● Assign tuple elements to multiple variables.
#● Example:
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a, b, c) # Output: 1 2 3

#4.Tuple Methods
#count(x) Counts the number of occurrences of x in the tuple

print((1, 2, 2, 3).count(2)) #2

#index(x) Returns the first index of x in the tuple 
print((1, 2, 3).index(2)) # 1

#5. Built-in Functions for Tuples
#len(tuple) Returns the length (number of elements) ofthe tuple
print(len((1, 2, 3))) #3

#max(tuple) Returns the maximum element in the tuple (forcomparable types)
print(max((1, 2, 3))) #3

#(tuple) Returns the minimum element in the tuple
print(min((1, 2, 3))) #1

#sum(tuple) Returns the sum of elements (if all arenumbers)
print(sum((1, 2, 3))) #6

#tuple(iterable)Converts an iterable (like a list or string) to atuple
print(tuple([1, 2, 3])) # (1, 2, 3)

#6. Immutability and Tuple Behavior
#Since tuples are immutable:
#● You cannot modify elements (tuple[0] = 10 will raise an error).● However, if a tuple contains mutable objects (e.g., lists), the mutable objects can stillbe changed.
#Example:
nested_tuple = (1, [2, 3])
nested_tuple[1][0] = 100
print(nested_tuple) # Output: (1, [100, 3])

#7. Advantages of Tuples
#1. Immutability: Ensures data cannot be accidentally modified.
#2. Faster: Tuples are more memory-efficient and faster than lists.
#3. Hashable: Tuples can be used as keys in dictionaries (unlike lists).
#4. Data Integrity: Ideal for storing constant data.

#8. Use Cases of Tuples
#● Returning multiple values from functions.
#● Representing fixed collections of items (coordinates, dates, etc.).
#● Using tuples as dictionary keys or set elements.

