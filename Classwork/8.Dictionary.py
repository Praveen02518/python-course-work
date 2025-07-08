#Dictionary
#A dictionary in Python is an ordered, mutable collection that stores key-value pairs.
# Unlike lists or tuples, which are indexed by position, dictionaries are indexed by unique keys.

#1. Introduction to Dictionary
#A dictionary is defined using curly braces {}, where each key is followed by a colon :, andthe key-value pairs are separated by commas.
#Syntax of a Dictionary:
#dictionary_name = {key1: value1, key2: value2, key3: value3}
#example
student = {
"name": "Alice",
"age": 21,
"course": "Computer Science"
}
print(student)

#2. Dictionary Operations
#These are the basic operations you can perform on dictionaries:
#2.1 Accessing Values
#Dictionaries allow access to values using keys.
print(student["name"]) # Output: Alice
print(student.get("age")) # Output: 21

#2.2 Adding and Updating Items
#You can add a new key-value pair or update an existing value by assigning a new value to akey.
student["age"] = 22 # Updating existing key
student["city"] = "New York" # Adding a new key-value pair
print(student)

#2.3 Removing Items from a Dictionary
#Using pop(key)
#Removes the specified key and returns its value.
age = student.pop("age")
print(age) # Output: 22
print(student)

#Using del
#Deletes a specific key-value pair or the entire dictionary.

del student["course"]
print(student)

#Using popitem()
#Removes and returns the last inserted key-value pair.
student.popitem()
print(student)

#Using clear()
#Removes all key-value pairs, making the dictionary empty.
student.clear()
print(student) # Output: {}

#3. Dictionary Built-in Methods
#3.1 Dictionary Methods for Accessing Data
#dict.get(key,default)
#dict.keys() 
#dict.values() 
#dict.values()
#dict.items() 

#3.2 Dictionary Methods for Adding and Updating Data

#Method Description Example
#dict.update(new_dict)
#dict.setdefault(key, default)

#3.3 Dictionary Methods for Removing Data
#dict.pop(key,default)
#dict.popitem() 
#dict.clear()
#del dict[key]

#4. Built-in Functions for Dictionaries
#Python provides several built-in functions that can be used with dictionaries.
#len(dict) Returns the number of items in thedictionary
#max(dict) Returns the maximum key (if keys arecomparable)
#min(dict) Returns the minimum key min({1: "a", 3: "b",2: "c"})
#sorted(dict)

#5. Nested Dictionaries
#A dictionary can contain another dictionary as its value.

students = {
"Alice": {"age": 21, "course": "CS"},
"Bob": {"age": 22, "course": "Math"}
}
print(students["Alice"]["course"]) # Output: CS

#6. Dictionary Comprehension
#You can create dictionaries dynamically using dictionary comprehension.

squares = {x: x*x for x in range(1, 6)}
print(squares) # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}



