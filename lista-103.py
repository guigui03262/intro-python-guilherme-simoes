#!/usr/bin/python3

'''
    DESAFIO!!!
    Implemente um algoritmo para inverter a ordem de uma string em sua
    linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''

print('-------------------------------------------------')
print('----------------EXERCICIOS-----------------------')
print('-------------------------------------------------')
print("\n") 
###
# Exercicios
###

book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

# 1) Extraia o titulo do livro da string
print("01")
q = book1.split("by")
q2 = book2.split("by")
q3 = book3.split("by Nassim")
print(q)
print(q2)
print(q3)

print("\n")

# 2) Salve o titulo de cada livro em uma variável
print("02")
v1 = q[0]
v2= q2[0]
v3 = q3[0]

v11 = q[1]
v22 = q2[1]
v33 = q3[1]

print(v1)
print(v2)
print(v3)

print("\n")

# 3) Quantos caracteres cada título tem?
print("03")
print("01 tem", len(v1), "caracteres")
print("02 tem", len(v2), "caracteres")
print("03 tem", len(v3), "caracteres")

print("\n")

# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}
print("04")
a1, y1 = v11.split(',')
a2, y2 = v22.split(',')
a3, y3 = v33.split(',')

f1 = '{0} - {1}, {2}'.format(v1, a1, y1)
f2 = '{0} - {1}, {2}'.format(v2, a2, y2)
f3 = '{0} - {1}, {2}'.format(v3, a2, y3)

print(f1)
print(f2)
print(f3)

print("\n")

# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta

palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'

print("05")

print(palindrome_one)
print(palindrome_one == palindrome_one[::-1])

palindrome_two2 = palindrome_two.lower() 
print(palindrome_two2)
print(palindrome_two2 == palindrome_two2[::-1])
    
palindrome_three2 = ''.join(palindrome_three.split())
print(palindrome_three2)
print(palindrome_three2 == palindrome_three2[::-1])
    
palindrome_four2 = ''.join(palindrome_four.split())
print(palindrome_four2)
print(palindrome_four2 == palindrome_four2[::-1])

print("\n")
