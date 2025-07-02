#1.Arithmetic Operators
a=20
b=10
print("Addition(+):",a+b) #Addition(+): 30
print("Subtraction(-):",a-b) #Subtraction(-): 10
print("Multiplication(*):",a*b) #Multiplication: 200
print("Division(/):",a/b) #Division (/):2.0
print("Floor division(//):",a//b) #Floor division(//):2
print("Modulus(%):",a%b) #Modulus(%): 0
print("Exponentiation(**):",a**b) #Exponentiation(**):10240000000000
#Exmples
a=20
b=10
print(a+b) #30 addition
print(a-b) #10 subtraction
print(a*b) #200 multiplication
print(a/b) #2.0 division
print(a//b) #2 floor division
print(a%b) #0 modulus
print(b%a) #10 modulus
print(a**b) #exponentiation

#2.Comparison operators
a=20
b=10
print("Equal to(==):",a==b) #Equal to(==)): False
print("Not Equal to(!=):",a!=b) #Not Equal to(!=)): True 
print("Greater than(>):",a>b) #Greater than(>)): True
print("Less than(<):",a<b) #Less than(<)): False
print("Greater than or Equal to(>=):",a>=b) #Greater than or Equal to(>=)): True
print("Less than or Equal to(<=):",a<=b) #Less than or Equal to(<=)): False
#Exmples
a=20
b=10
print(a==b) #Equal to(==): False
print(a!=b) #Not Equal to(!=): True
print(a>b) #Greater than(>): True
print(a<b) #Less than(<): False
print(a>=b) #Greater than or Equal to(>=): True
print(a<=b) #Less than or Equal to(<=): False

#3.Assignment operators
a=20
b=10
a=b
print("Assign(=):",a) 
a+=b
print("Add & Assign(+=):",a)
a+=b
print("Subtract & Assign(-=):",a) 
a-=b
print("Multiply & Assign(*=):",a)
a*=b
print("Divide & Assign(/=):",a) 
a/=b
print("Floor divide & Assign(//=):",a) 
a//=b
print("Modulus & Assign(%=):",a) 
a%=b
print("EXponentiate & Assign(**=):",a)
a**=b

#4.Logical Operators
a=10
b=20
#AND gate
print(a>5 and b<30) #true (both conditions are true)
#OR Gate
print(a>15 or b<30) #True (atleast one condition is true)
#NOT gate
print(not(a>5)) #false (reverse the true condition)

#5.Memership operators
names={"praveen","vasu","reo"}
#In operator
print ("praveen" in names) #true value exists in sequence
#Not in operator
print("ravi" not in names) #true value not exists in sequence
print("ravi" in names) #false not mentioned in names

#6.Identity operators
a=[1,2,3]
b=a
c=[1,2,3]
#Is operator
print(a is b) #true both refer to same object
print(a is c) #false different objects with same content
#Is not operator
print(a is not c) #true
print(b is not c) #true
print(b is c) #false

#7.Bitwise operators(with Binary Representation)










