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
    
       
 
 
