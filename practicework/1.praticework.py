#examples p and n
num=int(input("Enter the number: "))
if num>0:
    print("positive number")
elif num<0:
    print("negative number")
else:
    print("zero") 

#even and odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")
    
#leap year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year!")
else:
    print(f"{year} is NOT a Leap Year.")
    
#string and type conversuion
date_input = input("Enter a date (dd/mm/yyyy): ")
day, month, year = date_input.split('/')
another_format = f"{year}/{month}/{day}"
print("Date in yyyy/mm/dd format:", another_format)

#even or odd winner
day = int(input("Enter the day as an integer: "))
if day % 2 == 0:
    print("Even Winner")
else:
    print("Odd Winner")
#
# List of names with duplicates
names = ["meena", "arun", "arun", "ravi", "jhon", "jhon"]
unique_names = list(dict.fromkeys(names))
print("Unique names in order:", unique_names)

#


    

       
 
 
