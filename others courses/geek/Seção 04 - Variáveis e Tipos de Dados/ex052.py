premio = float(input('Valor do Premio: '))
amigo1 = int(input('Contibuição do 1º Amigo: '))
amigo2 = int(input('Contibuição do 2º Amigo: '))
amigo3 = int(input('Contibuição do 3º Amigo: '))
total_aposta = amigo1+amigo2+amigo3
p_amigo1 = amigo1/total_aposta
p_amigo2 = amigo2/total_aposta
p_amigo3 = amigo3/total_aposta
print(f'Amigo1 investiu {p_amigo1*100:3.1f}% ganhou R$ {premio*p_amigo1:.2f}')
print(f'Amigo2 investiu {p_amigo2*100:3.1f}% ganhou R$ {premio*p_amigo2:.2f}')
print(f'Amigo3 investiu {p_amigo3*100:3.1f}% ganhou R$ {premio*p_amigo3:.2f}')



