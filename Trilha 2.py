# Desafio Extra 0:
# Escreva um código que solicite ao usuário uma temperatura em Celsius e converta em Farenheit e vice versa.
celsius = float(input('Digite um valor de temperatura em Grau Celsius:'))
print(f'Essa temperatura em Grau Farenheit é: {celsius*1.8+32}')
farenheit = float(input('Digite um valor de temperatura em Grau Farenheit:'))
print(f'Essa temperatura em Grau Celsius é: {(farenheit-32)/1.8}ºC')

# Desafio Extra 1:
# Escreva um algoritmo solicite ao usuário um valor (total) em dinheiro, e informe quantas notas de: 1 real, 5 reais, 10 reais, 50 reais e 100 reais serão necessárias para compor este valor, de forma que seja utilizado o menor número de notas possíveis.
valortotal = int(input('Insira o valor total do seu dinheiro:'))

notas100 = valortotal // 100
if notas100 >= 1:
    valortotal -= notas100 * 100
    print(f'Você receberá {notas100} nota(s) de 100 reais')

notas50 = valortotal // 50
if notas50 >= 1:
    valortotal -= notas50 * 50
    print(f'Você receberá {notas50} nota(s) de 50 reais')

notas10 = valortotal // 10
if notas10 >= 1:
    valortotal -= notas10 * 10
    print(f'Você receberá {notas10} nota(s) de 10 reais')

notas5 = valortotal // 5
if notas5 >= 1:
    valortotal -= notas5 * 5
    print(f'Você receberá {notas5} nota(s) de 5 reais')

notas1 = valortotal // 1
if notas1 >= 1:
    valortotal -= notas1 * 1
    print(f'Você receberá {notas1} nota(s) de 1 reais')

# Desafio Extra 2:
# Crie um algoritmo que leia quatro números e imprima o cubo e a raiz quadrada de cada número.
num1 = float(input('Insira o primeiro número:'))
print(f'O primeiro número elevado ao cubo e sua raiz quadrada são, respectivamente: {num1**3}; {num1**0.5}')
num2 = float(input('Insira o segundo número:'))
print(f'O segundo número elevado ao cubo e sua raiz quadrada são, respectivamente: {num2**3}; {num2**0.5}')
num3 = float(input('Insira o terceiro número:'))
print(f'O terceiro número elevado ao cubo e sua raiz quadrada são, respectivamente: {num3**3}; {num3**0.5}')
num4 = float(input('Insira o quarto número:'))
print(f'O quarto número elevado ao cubo e sua raiz quadrada são, respectivamente: {num4**3}; {num4**0.5}')