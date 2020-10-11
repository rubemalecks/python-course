'''Exercício Python 004: 
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
 e todas as informações possíveis sobre ele.
 '''

a = input('Digite algo: ')
print('O tipo primitivo é', type(a))
print('Só tem espaços?',a.isspace())
print('É numero?', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanumerico?', a.isalnum())
print('Esta em letras maiusculas?', a.isupper())
print('Esta em letras minusculas?', a.islower())
print('Esta capitalizada?', a.istitle())
