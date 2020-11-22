'''x = 'rubem'
def func():
    x = 'álecks'
    print(x) # vai retornar "rubem", pois a função não altera a variavel global e sim a local
'''
'''#alterando variavel global
x = 'rubem'
def func():
    global x
    x = 'álecks'
    print(x)
func()
'''
#a forma ideal seria:

def func (arg=None): #arg=None deixa o argumento vazio para receber a entrada do usr
    arg = arg.replace('e', 'i')
    return arg
print(func(arg='Rubem'))