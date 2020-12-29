#dividir premio de loteria
from time import sleep
print('#'*30)
print('PREMIO DA LOTERIA')
print('#'*30)
sleep(1.5)
premio = float(780000)
print(f'Total {premio}')
ganhador1 = premio * 0.46
ganhador2 = premio * 0.32
ganhador3 = premio - (ganhador1 + ganhador2)

print(f'O 1º Ganhador Ficou com R${ganhador1:.2f}')
print(f'O 2º Ganhador Ficou com R${ganhador2:.2f}')
print(f'O 3º Ganhador Ficou com R${ganhador3:.2f}')
