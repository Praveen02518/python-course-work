#for loop and while loop
num=int(input("Enter the table number: "))

for i in range(1,21):
    print(f'{num} * {i} = {num*i}')
#
s='Praveen Harshith Vaeun Sheshu'.lower()
n=len(s) 
ch=input("Enter the char: ").lower()

for i in range(n):
     if s[i]==ch:
         print(ch,i)
#                     
products=['cycle','laptop','bike']      
items=input("Enter the items:").split()
for i in items:
    if i in products:
        print(products.index(i),i)
    else:
        print(f"{i} is not available")

#while loop
email,pwd='xyz@gmail.com','xyz@123'

max_attempts=5
while max_attempts>0:
    useremail=input("Enter the email: ")
    password=input("Enter the password: ")
    if useremail==email and pwd==password:
        print("login succesfull")
        break
    else:
        print("invalid login")    
        
    
        
