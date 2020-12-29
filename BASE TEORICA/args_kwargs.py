
def func (*args, **kwargs):
    print(args)

    idade = kwargs.get('idade') # .get quando não se sabe se o arg foi passado
   
    if idade is not None:
        print(idade)
    # ou 
    #print(kwargs['idade'])

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda', idade='27')
