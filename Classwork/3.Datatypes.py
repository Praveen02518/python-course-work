'''NUMERICAL TYPES'''

a=1
print(type(a)) #<class 'int'>

b=1.2
print(type(b)) #<class 'float'>

c=3+4j
print(type(c)) #<class 'complex'>

'''SEQUENCE TYPES'''

Name = "Praveen"
print(type(Name)) #<class 'str'>

Skills = ['Python','SQL','PowerBI']
print(type(Skills)) #<class 'list'>

Student = ("Praveen",692,"Data Analytics") 
print(type(Student)) #<class 'tuple'>
print("Name:",Student[0]) #Name: Praveen
print("ID:",Student[1]) #ID: 692
print("Department:",Student[2]) #Department: Data Analytics

'''SET TYPES'''

Colors = {"Blue", "Black", "White"} 
print(type(Colors)) #<class 'set'>

Cars = frozenset(["Audi","BMW","TATA"])
print(type(Cars)) #<class 'frozenset'>

'''MAPPING TYPE'''
Details = {"Name": "Praveen", "Batch": '14', "Course": "DA"}
print(type(Details)) #<class 'dict'>

'''BOOLEAN TYPE'''

A = True
B = False
print(type(A)) #<class 'bool'>
print(type(B)) #<class 'bool'>

'''NONE TYPE'''

Wish = None
print(type(Wish)) #<class 'NoneType'>