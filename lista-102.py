#!/usr/bin/python3

days_list = ['mon','tues','wed','thurs','fri', 'sat', 'sun']

list = ['a', 1, 3.14159265359]

print('-------------------------------------------------')
print('----------------EXERCICIOS-----------------------')
print('-------------------------------------------------')
print("\n") 
# list.reverse()
# print(list)

#########
# Exercicios - Listas
# Faca sem usar loops
#########

# Como selecionar 'wed' pelo indice?
print("01")
print(days_list[2])

print("\n")

# Como verificar o tipo de 'mon'?
print("02")
print(days_list[0])
print(type(days_list[days_list.index('mon')]))

print("\n")

# Como separar 'wed' até 'fri'?
print("03")
print(days_list[2:5])

q= days_list.index('wed')
w= days_list.index('fri')+1
print(days_list[q:w])

print("\n")

# Quais as maneiras de selecionar 'fri' por indice?
print("04")
print(days_list[4])

print("\n")

# Qual eh o tamanho dos dias e days_list?
print("05")
print(len(days_list))

print("\n")

# Como inverter a ordem dos dias?
print("06")
days_list.reverse()
print(days_list)

print("\n")

# Como inserir a palavra 'zero' entre 'a' e 1 de list?
print("07")
list = ['a', 1, 3.14159265359]
list.insert(1,"zero")
print(list)

print("\n")

# Como limpar list?
print("08")
list.clear()
print(list)

print("\n")

# Como deletar list?
print("09")
del(list)

print("\n")

# Como atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?
print("10")
list = ['a', 1, 3.14159265359]
ultimo_elemento = list.pop()
print(list)
print(ultimo_elemento)

print("\n")
