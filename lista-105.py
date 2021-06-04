#!/usr/bin/python3


'''
    DESAFIO!!!
    1) Crie uma lista com os 1000 primeiros numeros pares. Não use loop!
    2) Crie uma lista com os numeros de 0 ate 99999999999999999999999999. Depois crie um loop para percorrer a lista ateh encontrar o primeiro multiplo de 5.
    OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''

###
# Exercicios
###

print('-------------------------------------------------')
print('----------------EXERCICIOS-----------------------')
print('-------------------------------------------------')
print("\n") 

## Usando a 
lista = ['a','b','c']
# 1) Faca um loop dentro de uma funcao que irah retornar: ['A','B','C']
print("01")
def upper(lista):
    for i in range(len(lista)):
            lista[i] = lista[i].upper()
    return lista
    
print (lista)
print(upper(lista))


print("\n") 

## Usando a 
lista2 = [0, 1, 7, 4, 5] 
# 2) Faca um loop dentro de uma funcao para retornar a soma de todos os elementos da listas. A funcao deve receber a lista como parametro.
print("02")
   
def soma(lista2):
    soma=0
    for i in range(len(lista2)):
        soma = lista2[i] + soma
    return soma
       
print (lista2)
print(soma(lista2))

print("\n")

# 3) Crie uma funcao que receba uma lista e retorne outra lista composta pelos os numeros impares da lista recebida
print("03")

def impar(lista2):
    lista3 = []
    for i in range(len(lista2)):
       if lista2[i]%2 != 0:
           lista3.append(lista2[i])
    return lista3

print (lista2)
print(impar(lista2))

print("\n")

## usando a 
string = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
# 4) Conte quantas palavras de tamanho >= 5 existe nessa string. Faca uma vez sem usar list comprehension e depois usando list comprehension.
print("04")
count = 0
for i in string.replace(',','').split(' '):
    if(len(i) >= 5):
        count+= 1
print(count)

string = string.replace(',','').split(' ')
string2 = [i for i in string if len(i) >= 5]
print(len(string2))

print("\n")
# 5) Usando list comprehension, crie uma lista com os multiplos de 3 de 0 ate 100
print("05")
lista = [x * 3 for x in range(100) if (x*3) <= 100]
print(lista)

print("\n")
# 6) Faca uma funcao para encontrar os numeros primos no intervalo [2, 10), mas nao utilize a clausula else do for
print("06")
def primos():
    for i in range(2, 10):
        if i % 2 != 0:
            print(i) 
primos()    
print("\n")