print('''
As tarifas de certo parque de estacionamento são as seguintes:
~ 1ª e 2ª hora - R$ 1,00 cada
~ 3ª e 4ª hora - R$ 1,40 cada
~ 5ª hora e seguintes - R$ 2,00 cada

O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo, quem estacionar durante 61 minutos pagará por duas horas, que é 
o mesmo que pagaria se tivesse permanecido por 120 minutos. Os momentos de chegada ao parque e partida deste são apresentados na forma de pares de
 inteiros, representando horas e minutos. Por exemplo, o par 12 50 representará "dez para a uma da tarde". Pretende-se criar um programa que, lidos
pelo teclado os momentos de chegada e de partida, escreva na tela o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida se dão
com intervalo não superior a 24 horas. Portanto, se uma dada hora de chegada for superior à de partida, isso não é uma situação de erro, antes 
significará que a partida ocorreu no dia seguinte ao da chegada.''')

from math import ceil
horario_entrada = input('Hora Entrada: ').split(':')
hora_entrada, min_entrada = int(horario_entrada[0]), int(horario_entrada[1])

minutagem_entrada = hora_entrada*60 + min_entrada 

horario_saida = input('Hora Saida: ').split(':')
hora_saida, min_saida = int(horario_saida[0]), int(horario_saida[1])

minutagem_saida = hora_saida*60 + min_saida


if hora_entrada > hora_saida: 
    minutos_est = (1440 - minutagem_entrada) + minutagem_saida # CASO A ENTRADA SEJA ANTES DA 00:00
elif hora_saida >= hora_entrada: 
    minutos_est = (minutagem_saida-minutagem_entrada)

horas_est = minutos_est / 60
minutos_est = minutos_est % 60
if horas_est <= 2:
    pagar = ceil(horas_est) * 1
elif horas_est <= 4:
    pagar = ceil(horas_est)* 1.40
else:
    pagar = ceil(horas_est) * 2

print(f'O veiculo ficou estacionado {int(horas_est)}hrs e {minutos_est:.0f}min\nTOTAL: R${pagar:.2f}')
