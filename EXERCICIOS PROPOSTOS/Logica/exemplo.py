'''x = 'rubem'
def func():
    x = 'álecks'
    print(x) # vai retornar "rubem", pois a função não autera a variavel global e sim a local
'''
#alterando variavel global
x = 'rubem'
def func():
    global x
    x = 'álecks'
    print(x)
func()