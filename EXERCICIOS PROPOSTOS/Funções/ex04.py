'''Fizz Buzz - Se o parametro da função for divisivel por 3, retorne fizz. 
Se o parametro da funçao for divisivel por 5, retorne buzz. 
Se o parametro da função for divisivel por 5 e 3, retorne FizzBuzz, 
caso contrário, retorne o numero enviado'''

def FizzBuzz(a):
    if a % 5  == 0 and a % 3 == 0 :
        return print(f'FizzBuzz, {a} é divisivel por 5 e 3')
    if a % 5 ==  0 :
        return print(f'Buzz, {a} é divisivel por 5')
    if a % 3 == 0 :
        return print(f'Fizz, {a} é divisivel por 3')
    return print(a)

from random import randint
for c in range(100):    
    aleatorio = randint(0,100)
    FizzBuzz(aleatorio)
