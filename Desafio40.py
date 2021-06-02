print('Vamos Calcular a Suas Notas!')
a = float(input('Digite a Nota 1: '))
b = float(input('Digite a nota 2: '))

media = float(a + b)/2

if media < 5:
    print('Sua média é de: {}. Você se Ferrou!'.format(media))
elif media >= 5 and media < 6.9:
    print('Sua média é de: {}. Você ainda tem Salvação.'.format(media))
else:
    print('Sua media é de: {}. Você teve Sorte.'.format(media))