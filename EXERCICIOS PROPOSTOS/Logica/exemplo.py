'''
funções (def) em python - *args **kwargs
Aula 16 (part 3)    '''
'''
def func(a1, a2, a3, nome=None): # nome=None, por default n=None
    print(a1, a2, a3, nome)      # a partir desse momento as variveis seguintes ->
func(8,6,7, nome='Rubinho')      #... precisam ter seusvalores tambem setados
'''
def func(*argumentos):
    print(argumentos)
    print(argumentos[0])
    print(argumentos[-1])

func(1,2,3,4,5)