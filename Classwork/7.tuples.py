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