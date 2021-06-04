#!/usr/bin/python3

'''
    DESAFIO!!!
    1) Implemente um algoritmo para trocar o conteudo de duas variáveis x e y.
    2) Agora faca sem utilizar uma terceira variavel temporaria.
    OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''

print('-------------------------------------------------')
print('----------------EXERCICIOS-----------------------')
print('-------------------------------------------------')
print("\n") 

# 1) Crie uma funcao que receba duas listas e verifique se elas são iguais. Cada elemento e sua ordem devem ser o mesmo. Retorne True ou False.
#
print("01")
lista1 = [1, 2, 3, 4]
lista2 = [1, 2, 3, 4]

def qwe(lista1, lista2):
    if(lista1 == lista2):
        return True
    else:
        return False
print (lista1,lista2)
print(qwe(lista1,lista2))

print("\n") 

# 2) Crie uma funcao que verifica se duas strings são palindromes perfeitas. Faca as 'limpeza'/sanitizacao necessarias.  Retorne True ou False.
#
print("02")

str = 'ovos'

def func(str):
    str = str.lower().replace(' ','')
    if(str == str[::-1]):
        return True
    else:
        return False

print(str)
print(func(str))

print("\n") 
# OBS.: Utilize apenas o que foi estudado ate agora