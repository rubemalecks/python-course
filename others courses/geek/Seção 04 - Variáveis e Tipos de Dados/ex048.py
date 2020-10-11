'CONVERSÃO DE SEGUNDOS EM PYTHON'


 # // DIVISÃO INTEIRA
 # % RESTO DA DIVISÃO

segundos = int(input('SEGUNDOS: '))
horas = segundos // 3600
segundos_restantes = segundos % 3600
minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

print(f'{horas} horas, {minutos} minutos, {segundos}segundos')
