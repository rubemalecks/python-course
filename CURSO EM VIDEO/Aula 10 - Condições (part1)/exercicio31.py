print('='*22, 'VIAGEM', '='*22)
km = float(input('Distancia percorrida (km): '))
if km <= 200 :
    vlr = km * 0.50
    print('A viagem custou ao todo R${:.2f}'.format(vlr))
else:
    vlr = km * 0.45
    print('A viagem custou ao todo R${:.2f}'.format(vlr))
