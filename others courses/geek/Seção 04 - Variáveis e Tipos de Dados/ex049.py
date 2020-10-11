horai = int(input('Hora: '))
minutosi = int(input('Minutos: '))
segundosi = int(input('Segundo: '))

tempo_exp = int(input('Tempo de Duração em Segundos: '))
horaf = tempo_exp // 3600
sobra = tempo_exp % 3600
minutosf = sobra // 60
segundosf = sobra % 60

hora = horaf + horai + ((minutosf + minutosi) // 60)
minutos = (minutosf + minutosi) % 60

segundos = segundosi + segundosf
print(f'{hora}hr, {minutos}min, {segundos}seg')


