from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('Olá, vamos jogar JOKEMPO?')
print('''Suas  opcões:
[0]PEDRA
[1]PAPEL
[2]TESOURA''')

jogador = int(input('Qual a Sua Jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('-=' * 11)
print('Computador Jogou {}'.format(itens[computador]))
print('Jogador Jogou {}'.format(itens[jogador]))
print('-=' * 11)


if computador == 0:#computador joguou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÀLIDA')

elif computador == 1:#computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÀLIDA')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÀLIDA')
