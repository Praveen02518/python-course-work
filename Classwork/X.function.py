def greet(name):
    return f"Hello, {name}!"

print(greet("Alice")) # Output: Hello, Alice!

#1. Built-in Functions
#These are pre-defined functions available in Python that perform common operations without requiring user implementation.
#Common Built-in Functions:
'''● print(): Outputs text to the console.
● len(): Returns the length of an iterable.
● abs(): Returns the absolute value of a number.
● max(): Returns the largest value from a set of numbers.
● sorted(): Returns a sorted list.'''

#Examples
print(len("Hello")) # Output: 5
print(abs(-10)) # Output: 10
print(max(1, 5, 3)) # Output: 5
print(sorted([3, 1, 4, 2])) # Output: [1, 2, 3, 4]

#2. User-Defined Functions
#These are functions created by the user to perform specific tasks. They allow programmers to implement custom logic for their applications.
#Example

def add(a, b):
    return a + b

print(add(5, 10)) # Output: 15