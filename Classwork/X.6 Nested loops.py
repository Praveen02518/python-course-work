#
n = 5 # Change this for different sizes
for i in range(n):
    for j in range(n):
        print('1', end=' ')
    print()
    
# right angled triangle
for i in range(n):
    for j in range(i + 1):
        print('*', end=' ')
    print()  
#   
#inverted rightangled triangle
for i in range(6, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()         
# pyramid
n = 5
for i in range(n):
    print(' ' * (n - i - 1) + '* ' * (i + 1)) 
#

          