#
n = 5 # Change this for different sizes
for i in range(n):
    for j in range(n):
        print('1', end=' ')
    print()

# Print each letter of 'VIKASH' in star pattern
letters = "VIKASH"
size = 7  # Fixed size for clear letter shapes
for letter in letters:
    input(f"\nPress Enter to print the letter '{letter}'...")
    print(f"\nLetter: {letter}\n")
    if letter == 'V':
        n = 10  # Height of the "V"
        for i in range(n):
            for j in range(2 * n):
                if j == i or j == 2 * n - i - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    else:
        for row in range(size):
            for col in range(size):
                if letter == 'I':
                    if row == 0 or row == size-1 or col == size//2:
                        print('*', end=' ')
                    else:
                        print(' ', end=' ')
                elif letter == 'K':
                    if col == 0 or (row+col == size//2) or (row-col == size//2):
                        print('*', end=' ')
                    else:
                        print(' ', end=' ')
                elif letter == 'A':
                    if (col == 0 or col == size-1) and row != 0 or row == 0 or row == size//2:
                        print('*', end=' ')
                    else:
                        print(' ', end=' ')
                elif letter == 'S':
                    if row == 0 or row == size//2 or row == size-1 or (col == 0 and row < size//2) or (col == size-1 and row > size//2):
                        print('*', end=' ')
                    else:
                        print(' ', end=' ')
                elif letter == 'H':
                    if col == 0 or col == size-1 or row == size//2:
                        print('*', end=' ')
                    else:
                        print(' ', end=' ')
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
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n-row):
        print("*",end=' ')
    print()
    
#    
n=int(input("Enter the size: "))
for row in range(n):
    for spa in range(row):
        print(" ",end=' ')
    for col in range(n-row):
        print("*",end=' ')   
    print()   
     
for row in range(n):
    print(' '*row,end='')
    print("*"*(n-row),end='')
    print()
  
#    
n=int(input("Enter the size: "))

for row in range(n):
    if row<=n//2:
        print('*'*(row+1),end=' ')
    else:
        print('*'*(n-row),end='')
    print()              
#
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        # Print '*' at the border, space inside
        if row == 0 or row == n-1 or col == 0 or col == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
#
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        # Print '*' at the border, space inside
        if row == 0 or row == n-1 or col == 0 or col == n-1 or row==n//2 or col==n//2:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
    
#
n=int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        # Print '*' at the border, space inside
        if row == col or row+col==n-1 :
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()  
#
n = int(input("Enter the size for 'P': "))
for row in range(n):
    for col in range(n//2+1):
        # Print '*' for the vertical bar, top, and middle of 'P'
        if col == 0 or (row == 0 and col < n//2) or (row == n//2 and col < n//2) or (col == n//2 and row > 0 and row < n//2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

#

          