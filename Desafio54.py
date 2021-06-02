#leia 7 anos de nascimentos e calcule quantas sao +18
from datetime import date
atual = date.today().year
somama = 0
somame = 0

for c in range(1,8):# total de 7 usuarios
    ano = int(input('Digita o Ano que a {}º Pessoa Nasceu: '.format(c)))
    idade = atual - ano #calcula idade
    if idade >= 18:
         somama += 1 #add ao contador
    else:
        somame += 1
print('Total +18: {}'.format(somama))
print('Total -18: {}'.format(somame))