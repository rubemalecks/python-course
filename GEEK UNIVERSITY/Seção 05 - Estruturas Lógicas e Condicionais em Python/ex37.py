print('''
As tarifas de certo parque de estacionamento são as seguintes:
~ 1ª e 2ª hora - R$ 1,00
~ 3ª e 4ª hora - R$ 1,40
~ 5ª hora e seguintes - R$ 2,00

O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste 
modo, quem estacionar durante 61 minutos pagará por duas horas, que é o
mesmo que pagaria se tivesse permanecido por 120 minutos. Os momentos de 
chegada ao parque e partida deste são apresentados na forma de pares de 
inteiros, representando horas e minutos. Por exemplo, o par 12 50 
representará "dez para a uma da tarde". Pretende-se criar um programa que,
lidos pelo teclado os momentos de chegada e de partida, escreva na tela 
o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida 
se dão com intervalo não superior a 24 horas. Portanto, se uma dada hora 
de chegada for superior à de partida, isso não é uma situação de erro, 
antes significará que a partida ocorreu no dia seguinte ao da chegada."
''')


while True:
    hora_entrada = input('Hora de Entrada(hr:mn): ').split(':')
    hora_entrada[0],hora_entrada[1]  = int(hora_entrada[0]), int(hora_entrada[1])
    if hora_entrada[0]> 23 or hora_entrada[0] < 0:
        print('Horario Inválido')
    elif hora_entrada[1] > 60 or hora_entrada[1] < 0:
        print('Horario Inválido')
    else:
        break
while True:
    hora_saida = input('Hora de Saida(hr:mn): ').split(':')
    hora_saida[0],hora_saida[1]  = int(hora_saida[0]), int(hora_saida[1])
    if hora_saida[0]> 23 or hora_saida[0] < 0:
        print('Horario Inválido')
    elif hora_saida[1] > 60 or hora_saida[1] < 0:
        print('Horario Inválido')
    else:
        break

if hora_entrada[0] <= hora_saida[0]:
    horas_pagar = (hora_saida[0] - hora_entrada[0], hora_saida[1] - hora_entrada[1]).split()
    #horas_pagar[0], horas_pagar[1] = int(horas_pagar[0]), int(horas_pagar[1])
print(type(horas_pagar))


