#!/usr/bin/python3

#111
print("01")
x = 1
y = 2

print(x)
print(y)

q = y
y = x
x = q
print("invertido")
print(x)
print(y)
print("\n")

#222

print("02")
w = 1
e = 2

print(w)
print(e)

def trocar(w, e):
    return e, w
w, e = trocar(w, e)

print("invertido")
print(w)
print(e)