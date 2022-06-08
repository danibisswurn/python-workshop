# Desafio 0:
# Crie um programa que cadastre notas de 3 unidades para um Aluno. No final, imprima a média da nota, indicando se o aluno passou de ano, caso a média das notas seja maior ou igual a 7. Caso contrário, indique que o aluno está reprovado.
nomealuno = input('Digite o nome do aluno:')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

mediaAluno = (nota1 + nota2 + nota3) /3 

print(f'Sua média é: {mediaAluno}')

if mediaAluno >= 7:
    print('E você está aprovado')
else:
    print('E você está reprovado')

# Desafio 1:
# Baseado no código a cima, modifique o código para que receba notas de 5 alunos diferentes. Além da nota, peça algumas informações como nome, idade e matrícula.
alunos = []

#for posicao in range(5):
#while True:
while len(alunos) < 5:
  print(f'Insira os dados do novo aluno.')
  aluno = {
      'nome': '',
      'idade': None,
      'matrícula': None,
      'notas': [],
  } 

  nome = input('Digite o nome do aluno: ')
  aluno['nome'] = nome
  idade = input('Digite a idade do aluno: ')
  aluno['idade'] = int(idade)
  matricula = input('Digite a matrícula do aluno: ')
  aluno['matrícula'] = int(matricula)

  for posicao in range(3):
    nota = float(input(f'Digite a {posicao+1}ª nota: '))
    aluno.get('notas').append(nota)

  alunos.append(aluno)

  #continuar = input('Deseja inserir mais um aluno? (s/n) ')
  #if continuar == 'n':
  #  break

for aluno in alunos:
  medianotas = round(((aluno.get('notas')[0] + aluno.get('notas')[1] + aluno.get('notas')[2]) / 3), 2)

  if medianotas >= 7:
    condicao = 'Aprovado(a)'
  else:
    condicao = 'Reprovado(a)'

  print(f"O(a) aluno(a): {aluno.get('nome')}, de {aluno.get('idade')} anos e matrícula {aluno.get('matrícula')}, teve como média final {medianotas} e está {condicao}.")


# Desafio 2:
# Crie um programa que liste 5 candidatos e deixe disponível a opção de votar, até que seja solicitado encerrar a votação. Ao final, imprima os votos de cada candidato, quem foi o candidato mais votado e o percentual de cada candidato.
candidatos = ['Felipe', 'Lula', 'Marina', 'José', 'Ciro']
votos = []

while True:
  print (candidatos)
  voto = input('Escolha seu candidato considerando as opções acima: ')
  votos.append(voto)
  continuar = input('Novo eleitor? (s/n) ')
  if continuar == 'n':
    break

for candidato in candidatos:
  totalvotos = votos.count(candidato)
  percentual = round(((totalvotos / len(votos)) * 100), 2)
  print(f'O candidato {candidato} teve {totalvotos} votos, o que equivale a {percentual}% dos votos.')

print(f'O(A) candidato(a) mais votado(a) foi o(a) {max(votos, key=votos.count)}!')

# Desafio 3:
# Criar um algoritmo que peça uma palavra ao usuário e conte quantas letras são vogais e quantas letras são consoantes.
vogais = []
consoantes = []

palavra = input('Digite uma palavra qualquer: ')

for letra in palavra:
    if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
        vogais.append(letra)
    else:
        consoantes.append(letra)

print(f'Essa palavra tem {len(vogais)} vogais e {len(consoantes)} consoantes.')

# Desafio 4:
# Criar um código que verifique se um número primo ou não.
numero = int(input('Digite um número: '))
divisores = 0

for divisor in range(1, (numero + 1)):        
  if numero % divisor == 0:
    divisores += 1
    
if divisores  == 2:
  print('Esse é um número primo')
else:
  print('Esse não é um número primo')

# Desafio 5:
# Criar um código que combine os valores dentro de um determinado array. Por exemplo: No array [1, 2], temos duas 3 combinações possíveis: (1, 1), (1, 2), (2, 2)
valores = [1, 2, 3]
combinacoes = []

for valor1 in valores:
    for valor2 in valores:
        if (valor1, valor2) not in combinacoes and (valor2, valor1) not in combinacoes:
            combinacoes.append((valor1, valor2))

print(combinacoes)

