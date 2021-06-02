n1 = int(input('Digite numero A: '))
n2 = int(input('Digite numero B: '))

if n1 > n2:
    print('Numero {} é maior que {}'.format(n1, n2))
elif n1 < n2:
    print('Numero {} é menor que {}'.format(n1, n2))
else:
    print('Numeros {} e {} sao iguais'.format(n1, n2))
