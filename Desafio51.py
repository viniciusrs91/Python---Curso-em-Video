print('-='*22)
print('Vamos realizar uma progressão Aritimética!')
print('-=' * 22)
p = int(input('Digite o Primeiro termo: '))
r = int(input('Digite a razao '))
dec = p + (10-1) * r

for c in range(p, dec + r, r):
    print(c, end=" - ")
print('ACABOU')
print('-=' * 22)
print('FIM')
