def contador(i,f,p): #pressionar crtl + shift + 2
    """
    [titulo de exemplo]

   
        i ([int]): [Inicio da contagem]
        f ([int]): [Fim da contagem]
        p ([int]): [passo ou pulo]
    """
    c = i
    while c <= f:
        print(c, end=' ')
        c+=p
    print('fim')
contador(0,100,10)
#print('-'*42)
#help(contador)

 
