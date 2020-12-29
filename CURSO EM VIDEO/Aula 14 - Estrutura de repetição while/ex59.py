"""
CHALLENGE 059: Creating an Options Menu
Create a program that reads two values ​​and shows a menu as below on the screen:
[1] Add
[2] Multiplication
[3] Higher number
[4] New Releases
[5] Exit Program
Your program must perform a requested operation in each case.
"""
from time import sleep
v1 = int(input('Enter a value: '))
v2 = int(input('Enter another value: '))
choice = 0
while choice != 5 :
    choice = int(input('''
    [1] Add
    [2] Multiplication
    [3] Higher number
    [4] New Releases
    [5] Exit Program
    \nChoice: '''))
    print('')
    print('='*27)
    print('Processing...'), sleep(2)
    if choice == 1 :
        v0 = v1 + v2
        print('The sum between {} and {} is = {}'.format(v1, v2, v0))
    elif choice == 2 :
        v0 = v1 * v2
        print('The Result between {} * {} is = {}'.format(v1, v2, v0))
    elif choice == 3 :
        if v1 > v2:
            print('{} is bigger than {}'.format(v1,v2))
        if v1 == v2:
            print('{} this the same as {}'.format(v1, v2))
        else:
            print('{} is bigger than {}'.format(v2,v1))
    elif choice == 4 :
        v1 = int(input('Enter a value: '))
        v2 = int(input('Enter another value: '))
    print('='*27)
if choice == 5 :
    print('Exiting...'), sleep(2)
print('Program completed!'), sleep(1)
