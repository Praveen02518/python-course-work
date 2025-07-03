#strings
str1 = 'Hello'
str2 = "World"
str3 = '''This is a multi-line string example.'''
print(str1)
print(str2)
print(str3)

#Operations on string
# Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result) # Output: Hello World
# Repetition
print("Python! " * 3) # Output: Python! Python! Python!
# Indexing
text = "Python"
print(text[0]) # Output: P (1st character)
print(text[-1]) # Output: n (last character)
# Slicing
print(text[0:3]) # Output: Pyt (from index 0 to 2)
print(text[:4]) # Output: Pyth (default start is 0)
print(text[2:]) # Output: thon (from index 2 to end)
# Membership
print('Pyt' in text) # Output: True
print('Java' not in text) # Output: True

#Built-in String Funtions
# 1. len()
text = "Hello World"
print(len(text)) # Output: 11
# 2. max() and min()
print(max("abcXYZ")) # Output: 'c' (highest ASCII value)
print(min("abcXYZ")) # Output: 'X' (lowest ASCII value)
# 3. sorted()
print(sorted("python")) # Output: ['h', 'n', 'o', 'p', 't','y']
# 4. chr() and ord()
print(ord('A')) # Output: 65 (ASCII value of 'A')
print(chr(97)) # Output: 'a' (character for ASCII value 97)

#1.Case Conversion Methods
#upper() Converts all characters to uppercase.
print("hello".upper()) #HELLO
#lower() Converts all characters to lowercase.
print("HELLO".lower()) #hello
#capitalize() Capitalizes the first character
print("python".capitalize()) #Python
#title() Capitalizes the first letter of each word.
print("hello world".title()) #Hello World
#swapcase() Swaps case: upper → lower, lower → upper.
print("PyThOn".swapcase()) #pYtHoN
#casefold() Converts to lowercase (more aggressive than lower()).
print("ß".casefold()) #ss

#2.Alignment & Formatting Methods
#center(width,fillchar)
print("python".center(10, "*")) #"*python*"
#ljust(width,fillchar)
print("py".ljust(5, "-")) #"py---"
#rjust(width,fillchar)
print("py".rjust(5, "-")) #"---py"
#zfill(width) Pads the string with zeros on the left.
print("42".zfill(5)) #"00042"
#format() Formats strings dynamically.
print("Name: {}, Age:{}".format("Tom", 25)) # "Name:Tom, Age: 25"
#format_map(mapping)
print("{name} is {age}".format_map({'name':'Tom', 'age': 25})) #"Tom is 25"

#3.Search & Find Methods
#find(sub)
print("hello".find("l")) #2
#rfind(sub) 
print("hello".rfind("l")) # 3
#index(sub) Like find(), but raises an error if not found.
print("hello".index("e")) # 1
#rindex(sub) Like rfind(), but raises an error if not found.
print("hello".rindex("l")) # 3
#count(sub) Counts how many times sub appears. 
print("banana".count("a")) # 3