# Recebendo os valores do usuário

a = float(input('Digite o primeiro numero:'))
b = float(input('Digite o segundo numero:'))

# Declarabdo as funcoes matematicas
def soma(a,b):
    return a + b
def subtracao(a,b):
    return a - b
def multiplicacao (a,b):
    return a * b
def divisao(a,b):
    if b!=0: return a / b
    else: return "Operação nula"

# Calculando e imprimindo os resultados
print(f'Resultado da adicao:  {soma(a,b)}')
print(f'Resultado da subtracao:  {subtracao(a,b)}')
print(f'Resultado da multiplicacao:  {multiplicacao(a,b)}')
print(f'Resultado da divisao:  {divisao(a,b)}')