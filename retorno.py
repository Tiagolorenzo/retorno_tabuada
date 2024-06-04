# Função tabuada
def calcular_tabuada(x, y):
    soma = x + y
    yield soma
    subtração = x - y
    yield  subtração
    multiplicacao = x * y
    yield  multiplicacao
    divisao = x / y
    yield divisao

# programa principal
x = int(input('Informe o primeiro número: '))
y = int(input('Informe o segundo número: '))
resultados = calcular_tabuada(x, y)

# exibe resultado na tela
print(f'A soma é {next(resultados)}.')
print(f'A subtracao é {next(resultados)}.')
print(f'A multiplicacao é {next(resultados)}.')
print(f'A divisao é {next(resultados)}.')

