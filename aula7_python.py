# -*- coding: utf-8 -*-
"""aula7_Python

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N_RU3NUGFd6OmCIqEnU4auxCInILF_Bz
"""

# n=10
# while n <=10:
#   print ('Hello')
#   n += 1

# contador = 1
# while contador <= 5:
#   print ('Numero: ', contador)
#   contador = contador + 1

# contador = 10
# while contador > 0:
#     print (contador)
#     contador -= 1
#     print ('contagem')

# senha_correta = "senha123"
# tentativas = 3

# while tentativas > 0:
#   senha = input("Digite a senha: ")
#   if senha == senha_correta:
#     print ("Acesso concedido.")
#     break # Sai do loop se a senha estiver correta
#   else:
#     tentativas -= 1
#     print (f"Senha incorreta. Tentativas restantes: {tentativas}")

# if tentativas == 0:
#   print ("Acesso Bloqueado.")

# nome = 'Ana'

# while nome == 'Ana':
#   print(f'Ola {nome}')
# else:
#   print(f'Ola {nome}')

# Exercicio 1

# n =  10
# while n >= 1:
#   print (n)
#   n -= 1
# print ('Fogo')


# Exercicio 2

# numero = int(input ("Digite um numero positivo:"))
# soma = 0
# c = 2
# while c <= numero:
#   soma += c
#   c += 2

# print(f"Soma dos numeros pares de {numero} é {soma}")

# Exercicio 3

# n = int(input ("Digite um numero inteiro:"))
# c = 0
# print('Tabuada do ' ,n)
# while c <=10:
#   r = n * c
#   print(f'{n}x{c} = {r} ')
#   c +=1

# Exercicio 4

# c = 99
# while c >= 1:
#      print (c)
#      c-=2

# import random


# n = random.random()*10
# print(n)


# n = random.randint(1,3)
# print(n)

# import random

# print ('''Jogo de Adivinhação
# Tente acertar o número da máquina
# Escolha um numero entre 1 e 10!''')

# numero_da_maquina = random.randint(1,10)
# chances = 3

# while chances > 0:
#     chute = int(input('Digite seu chute: '))
#     if chute == numero_da_maquina:
#      print ('Sensacional, você acertou')
#      break
#     else:
#       chances -=1
#       print (f'Você errou')
# else:
#   print ('Suas chances acabaram')


# Exercicio 1

# import random

# n = random.randint (5,10)
# print(n)

# Exercicio 2

import random

n1 = random.randrange(1,10)
n2 = random.randint(1,10)
n3 = random.randint(1,10)
print(n1, n2, n3)


# Exercicio 3

# import random

# n = random.randrange(10,30)
# print (n)