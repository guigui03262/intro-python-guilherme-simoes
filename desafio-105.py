#!/usr/bin/python3

#111
print("01")
x = 0
lista = []

def numPares(x):
    if x % 2 == 0:
        lista.append(x)
        x = x + 1
    
    else:
        x = x + 1
    
    if x == 0 or len(lista) == 1000:
        return 1
    
    else:
        numPares(x)
    

numPares(x) 
print(lista)
print("\n")

#222
print("02")
        
for x in range(99999999999999999999999999):
    if(x//5):
        print(x)
        break