#!/usr/bin/python3

professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}
print(type(professor1))
print(professor1)
print(len(professor1))
print(professor1.keys())
print(professor1.values())

professor2 = {'id': 37, 'name': 'Denilson Barbosa', 'age': 40, 'state_origin': 'Paraná', 'courses': ['Inteligência Artificial', 'Banco de Dados I', 'Banco de Dados II', 'Programação para Internet I']}
print(professor2['courses'][0])


professor3 = dict(id=28, name='Jorge Armino', idade=37)
print(type(professor3))
print(professor3)

professor3['state_origin'] = 'Rio Grande do Sul'
professor3['courses'] = ['Filosofia', 'Informática e Sociedade']
print(professor3)


print(professor1['state_origin'])



list = [2, 3, 5, 7, 11, 13, 17, 19]

tuple = (2, 3, 5, 7, 11, 13, 17, 19)

###
# Exercicio
###

print('-------------------------------------------------')
print('----------------EXERCICIOS-----------------------')
print('-------------------------------------------------')
print("\n")

# 1) Imprima os metodos disponiveis para uma lista e para uma tupla
print("Lista:", list)
print("\n")

print("Inserindo no final")
list.append(22)
print(list)

print("Inserindo em determinado lugar")
list.insert(0, 0)
print(list)

print("Concatenando")
list.extend(list)
print(list)

print("Removendo")
list.remove(0)
print(list)

print("Remove no indice passado")
list.pop()
print(list)

print("Descobrindo o index do numero 3")
print(list.index(3))

print("contando as vezes q o 3 aparece")
print(list.count(3))

print("Invertendo")
list.reverse()
print(list)

print("Ordenando")
list.sort()
print(list)
print("\n")

print("Tupla:", tuple)
print("\n")

print("Tupla é um tipo de estrutura de dados utilizada em Python que funciona de modo semelhante a uma lista, entretanto, com a característica principal de ser imutável. Isso significa que quando uma tupla é criada não é possível adicionar, alterar ou remover seus elementos. Geralmente, ela é utilizada para adicionar tipos diferentes de informações, porém, com a quantidade de elementos definidos.")


print("Descobrindo o index do numero 3")
print(tuple.index(3))

print("contando as vezes q o 3 aparece")
print(tuple.count(3))
print("\n")
# tuple.append(22)
# tuple.extend(tuple)
# tuple.insert(0, 0)
# tuple.remove(0)
# tuple.pop()
# tuple.reverse()
# tuple.sort()

# 2) Faca um metodo para retornar apenas as diferencas entre as duas de metodos
lista = 9
tupla = 2
print("A diferença e de: ", lista - tupla)

print("\n")
# 3) Adicione as coordenadas (latitude, longitude) para os dicts professor1, professor2 e professor3. Copie os dicts do arquivo 106.py. As coordenadas precisam ser inseparaveis e imutaveis.

professor1['Latitude/Longitude'] = ('90','0')
professor2['Latitude/Longitude'] = ('1','2')
professor3['Latitude/Longitude'] = ('2','1 ')

print(professor1)
print(professor2)
print(professor3)
