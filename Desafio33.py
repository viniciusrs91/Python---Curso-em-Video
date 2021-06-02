# entra 3 numeros e mostra o maior e o menor
a = int(input('Digite o Primeiro Número: '))
b = int(input('Digite o Segundo Número: '))
c = int(input('Digite o Terceiro Número: '))

if a > b and a > c:
    print('O Número {} é o Maior numero.'.format(a))
elif b > a and b > c:
    print('O Número {} é o Maior numero.'.format(b))
else:
    print('O Número {} é o Maior numero.'.format(c))
if a < b and a<c:
    print('O Número {} é o Menor numero.'.format(a))
elif b < a and b < c:
    print('O número {} é o menor numero'.format(b))
else:
    print('O numero {} é o menor Número.'.format(c))