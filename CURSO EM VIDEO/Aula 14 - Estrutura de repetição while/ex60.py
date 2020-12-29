"""
CHALLENGE 060: Factorial Calculation
Make a program that reads any number and shows your factorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""

number = int(input('Digite: '))
factorial = number
result = number
add = ''
print(str(number)+'!', end=' => ')
print(number, end='')
while factorial > 0 :   
    if factorial > 1:
        print(' x ', end='')
    if factorial != number : 
        result *= factorial
    factorial -= 1
    if factorial >= 1 :
        print(factorial, end='')         
print(' = {}'.format(result))