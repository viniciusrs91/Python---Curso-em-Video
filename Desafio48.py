s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s = s + c

print('''A Soma dos {} numeros 
impares divididos por 3 de 1 a 500 é: {}'''.format(cont, s))
