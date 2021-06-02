s = 0
x = 0 # contador
for c in range(1, 7):
    n = int(input('Digite o {} valor: '.format(c)))
    if n % 2 == 0:
        s += n
        x += 1

print('A soma dos {} valores PARES é igual a {}.'.format(x, s))
