'''try:
    file= open('demo.txt', 'r')
except FileNotFoundError:
    print("file is not present") 
else:
    read= file.read()
    file.seek(0) 
    readlines=file.readlines()
    file.seek(0) 
    readline=file.readline() 
    print(f"\nFile Content using read():\n{read}")
    print(f"\nFile Content using readlines():\n{readlines}")
    print(f"\nFile Content using readline():\n{readline}")
    file.close()
finally:
    print("Rest of the code")  

try:
    file= open('dsda.txt', 'w+')
except FileNotFoundError:
    print("file is not present") 
else:
    file.write('Monday we have exam\n')
    file.seek(0)
    print(file.read())
    file.close()
finally:
    print("Rest of the code")    

with open('dsda.txt','r+') as file:
    file.write('\nfile operations')
    file.seek(0)
    print(file.read())
    print("Rest of the code")  '''
    
import os
import shutil

if not os.path.exists('DSDA'):
    os.mkdir('DSDA')
    os.makedirs('DSDA/1415')   

#os.rmdir('DSDA')
shutil.rmtree('DSDA')     
