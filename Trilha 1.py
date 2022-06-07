#Desafio 0
# Escreva um código que solicite ao usuário o seu nome e imprima na tela uma mensagem de “Boas-vindas” com o nome indicado
nome = input("Digite seu nome: ")
print(f'Seja bem-vinda, {nome}.')

#Desafio 1
# Escreva um programa que pergunte os seguintes dados referentes ao pneu de um automóvel:
# P = pressão
# V = volume
# T = temperatura
# Calcule e imprima a massa de ar desse pneu segundo a fórmula (PV = 0.37M(T + 460)), onde M representa a massa de ar
P = float(input('Qual o valor da pressão?'))
V = float(input('Qual o valor do volume?'))
T = float(input('Qual o valor da temperatura'))
M = 0.0

y = P*V
x = 0.37*(T+460)
M = y/x
print(f'A massa de ar do pneu é de {M}')

#Desafio 2
# O IMC – Índice de Massa Corporal é um critério da Organização Mundial de Saúde para dar uma indicação sobre a condição de peso de uma pessoa adulta.
# A fórmula é IMC = peso / (altura)²
# Elabore um algoritmo que leia o peso e a altura e imprima o IMC calculado
peso = float(input('Qual o valor do seu peso?'))
altura = float(input('Qual o valor da sua altura?'))
imc = peso / (altura **2)

print(f'O seu Índice de Massa Corporal é {imc}')

#Desafio 3
# Utilizando como base o Desafio 2, complemente o algoritmo informando ao usuário a categoria da pessoa, com base na seguinte tabela:
# IMC em adultos	Condição
# Abaixo de 18,5	Abaixo do peso
# Entre 18,5 e 25	Peso normal
# Entre 25 e 30	Acima do peso
# Acima de 30	Obeso
peso = float(input('Qual o valor do seu peso?'))
altura = float(input('Qual o valor da sua altura?'))
imc = peso / (altura **2)

if imc < 18.5:
    condicao = 'abaixo do peso'
elif imc >= 18.5 and imc < 25:
    condicao = 'dentro do peso'
elif imc >= 25 and imc <= 30:
    condicao = 'acima do peso'
elif imc > 30:
    condicao = 'obeso'
    
print(f'O seu Índice de Massa Corporal é {imc}, e você está {condicao}.')

# Desafio 4
# Construa um algoritmo que leia um número e, se ele for maior do que 20, então imprima a metade do número.
num = int(input('Insira um número:'))
if num > 20:
    condicao = num/2
print(f'A metade do número inserido é: {condicao}')

# Desafio 5
# Escreva um algoritmo que leia um número e informe se ele é divisível por 10, por 5, por 2 ou se não é divisível por nenhum destes.
num = int(input('Insira um número:'))
condicao10 = False
condicao5 = False
condicao2 = False

if num % 10 == 0:
    condicao10 = True
    print('Esse número é divisível por 10')
if num % 5 == 0:
    condicao5 = True
    print('Esse número é divisível por 5')
if num % 2 == 0:
    condicao2 = True
    print('Esse número é divisível por 2')

if condicao10 == False and condicao5 == False and condicao2 == False:
    print('Este número não é divisível por 10, 5 ou 2.')

# Desafio 6
# Criar um algoritmo que leia dois números e imprima uma mensagem dizendo se são iguais ou diferentes.
num1 = int(input('Insira o primeiro número:'))
num2 = int(input('Insira o segundo número:'))

if num1 == num2:
    print('Esses números são iguais.')
if num1 != num2:
    print('Esses números são diferentes.')

# Desafio 7
# Desenvolva um algoritmo que leia três números e armazene o maior número na variável de nome MAIOR.
maior = None

num1 = int(input('Insira o primeiro número:'))
maior = num1

num2 = int(input('Insira o segundo número:'))
if num2 > maior:
    maior = num2

num3 = int(input('Insira o terceiro número:'))
if num3 > num2:
    maior = num3 

print(f'{maior}')

# Desafio 8
# Construa um algoritmo que indique se o número digitado está compreendido entre 20 e 90 ou não.
numero = int(input('Insira um número:'))

if numero >= 20 and numero <= 90:
    print('Esse número está compreendido entre os números 20 e 90.')

else:
    print('Esse número não está compreendido entre os números 20 e 90.')

# Desafio 9
# Ler um número e imprimir se ele é igual a 5, 200, a 400, se está no intervalo entre 500 e 1000, inclusive, ou se ele está fora dos escopos anteriores.
numero = int(input('Insira um número:'))

if numero >= 500 and numero <= 1000:
    print('Esse número está dentro do intervalo 500 e 1000, e não é igual a 5, 200 ou 400.')

elif numero == 5 or numero == 200 or numero == 400:
    print('Esse número é igual a 5, 200 ou 400, e não está dentro do intervalo 500 e 1000.')

elif numero != 5 or numero != 200 or numero != 400 or numero <500 or numero > 1000:
    print('Esse número não está dentro do intervalo 500 e 1000, e também não é igual 5, 200 ou 400.')

# Desafio 10
# Depois da liberação do governo para as mensalidades dos planos de saúde, as pessoas começaram a fazer pesquisa para descobrir um bom plano, não muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir. Crie um algoritmo que entre com o nome e a idade de uma pessoa e imprimir o nome e o valor que ela deverá pagar.
# Até 10 anos – R$ 30,00
# Acima de 10 até 29 anos – R$ 60,00
# Acima de 29 até 45 anos – R$ 120,00
# Acima de 45 até 59 anos – R$ 150,00
# Acima de 59 até 65 anos – R$ 250,00
# Maior que 65 anos – R$ 400,00
nome = (input('Qual o seu nome?'))
idade = int(input('Qual a sua idade?'))

if idade <= 10:
    condicao = 'R$ 30,00'
elif idade > 10 and idade <= 29:
    condicao = 'R$ 60,00'
elif idade > 29 and idade <= 45:
    condicao = 'R$ 120,00'
elif idade > 45 and idade <= 59:
    condicao = 'R$ 150,00'
elif idade > 59 and idade <= 65:
    condicao = 'R$ 250,00'
elif idade > 65:
    condicao = 'R$ 400,00'
print(f'{nome}, o valor que você deverá pagar é de {condicao}.')