#!/usr/bin/python3
import csv
import gzip
import shutil

professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}
print(type(professor1))
print(professor1)
print("\n") 

professor2 = {'id': 37, 'name': 'Denilson Barbosa', 'age': 40, 'state_origin': 'Paraná', 'courses': ['Inteligência Artificial', 'Banco de Dados I', 'Banco de Dados II', 'Programação para Internet I']}
print(professor2)
print("\n") 

professor4 = {'id': 1, 'name': 'teste', 'state_origin': 'Amazonas'}
print(professor4)
print("\n")

# Utilizando construtor
professor3 = dict(id=28, name='Jorge Armino', idade=37)
print(type(professor3))
print(professor3)
print("\n") 

# adicionando chave e valor em um dict jah existente
professor3['state_origin'] = 'Rio Grande do Sul'
professor3['courses'] = ['Filosofia', 'Informática e Sociedade']
print(professor3)
print("\n") 


###
## Exercicios
###
print('-------------------------------------------------')
print('----------------EXERCICIOS-----------------------')
print('-------------------------------------------------')
print("\n") 

# 1) Implemente o metodo define_default_city de acordo com a docstring definida no inicio da funcao. Utilize a clausula else no loop implementado.
print("01")

"""def define_default_city(state):
    ''' Define a capital do estado de origem como city_origin para um professor existente no arquivo. Retorna True se a capital do estado de origem existe no arquivo capitais-BR.csv e False, caso contrario.
    Keyword arguments:
        state -- O estado de origem do professor
    '''
    pass
"""

def define_default_city(state):
	arquivo = open('capitais-BR.csv', 'r', encoding='utf8')
	for linha in arquivo:
		if state in linha:
			return True
	return False
	arquivo.close()

print(define_default_city(professor4['state_origin']))
print(professor4)
print("\n") 


# 2) Remova do arquivo capitais-BR.csv todas capitais dos estados do sudeste e teste se sua funcao estah robusta o suficiente. Ela deve executar sem erro mesmo que alguns dados estejam faltando.
print("02")

def remover():
    with open('capitais-BR.csv', 'r', encoding="utf8") as cap:
        ler = csv.reader(cap, delimiter=';')
        tirar = list(ler)

        try:
            tirar.remove(['Espírito Santo', 'Vitória'])
            tirar.remove(['Minas Gerais', 'Belo Horizonte'])
            tirar.remove(['Rio de Janeiro', 'Rio de Janeiro'])
            tirar.remove(['São Paulo', 'São Paulo'])
            with open("capitais-BR.csv", 'w', encoding='utf8', novalinha='') as novo:
                writer = csv.writer(novo)
                writer.writerows(tirar)         
        except:
            print('ja foi tirado')

    
        
#remover()
print("\n") 

# 3) Faca uma funcao que le o arquivo lista-cpf.txt, retorne a quantidade de CPF unicos (sem repeticao) e os escreva em um arquivo lista-cpf-unicos.txt. Eh necessario descompactar o arquivo lista-cpf.txt.tar.gz primeiro. O algoritmo precisa ser eficiente, nesse caso especifico a melhor a melhor complexidade que pode ser acancada é linear. Algoritmos de complexidade quadratica, cubica, fatorial, etc. não sao considerados como eficientes pois a complexidade linear eh garantida. Como regra geral, se seu algoritmo demorar mais do que alguns segundos, ele, provavelmente, nao eh linear.
print("03")

def descompactar():
    with gzip.open("lista-cpf.txt.tar.gz", 'r') as entrada:
        with open('cpfs.txt', 'wb') as saida:
            shutil.copyfileobj(entrada, saida)




print("\n") 