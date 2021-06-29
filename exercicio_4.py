from math import sin, cos, tan, exp

def funcao(x):
    valor = eval(func)
    return valor

def primeira_derivada(xi,dx):
    valor_primeira_derivada = (funcao(xi + dx) - funcao(xi - dx)) / 2*dx
    return valor_primeira_derivada

def segunda_derivada(xi,dx):
    valor_segunda_derivada = (funcao(xi + dx) - 2*funcao(xi) + funcao(xi - dx)) / (dx**2)
    return valor_segunda_derivada

func = input("Insira a função a ser derivada ex: ( 4*x**2 + sin(x) - exp(x) ): ")
ponto = float(input("Insira o ponto no qual voce deseja saber a derivada: "))
dx = float(input("Insira o valor do incremento: "))

derivada_1 = primeira_derivada(ponto,dx)
derivada_2 = segunda_derivada(ponto,dx)
valor_funcao = funcao(ponto)

print('valor da função no ponto: '  + str(valor_funcao))
print('valor da primeira derivada no ponto: '  + str(derivada_1))
print('valor da segunda derivada no ponto: '  + str(derivada_2))