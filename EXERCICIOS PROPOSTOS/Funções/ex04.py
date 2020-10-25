'''Fizz Buzz - Se o parametro da função for divisivel por 2, retorne fizz. 
Se o parametro da funçao for divisivel por 5, retorne buzz. 
Se o parametro da função for divisivel por 5 e 3, retorne FizzBuzz, 
caso contrário, retorne o numero enviado'''

def FizzBuzz(a):
    if a % 5  == 0 and a % 3 == 0 :
        return print(f'FizzBuzz, {a} é divisivel por 5 e 3')
    elif a % 5 ==  0 :
        return print(f'Buzz, {a} é divisivel por 5')
    elif a % 2 == 0 :
        return print(f'Fizz, {a} é divisivel por 2')
    else:
        return print(a)

for c in range(100):    
    from random import randint
    aleatorio = randint(1,100)
    FizzBuzz(aleatorio)