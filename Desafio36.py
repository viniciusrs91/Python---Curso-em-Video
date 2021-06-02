cores = {'fimcor': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m',
         'vermelho': '\033[31m'}

print('Olá, seja bem vindo ao {}HOUSE-SIMULATOR 3000{}'.format(cores['amarelo'],cores['fimcor']))
valor = float(input('Digite o Valor do Imovél: R$  '))
salario = float(input('Digite o seu Salário: '))
anos = int(input('Em Quantos Anos deseja pagar?: '))

meses = anos * 12

total = valor/meses
porcentagem = salario * 30/100

if total > porcentagem:
    print('Seu Financiamento {}NÃO foi APROVADO {} pois,'
          '\no valor da parcela mensal de {}${:.2f}{} excede 30% do Sálario {}${:.2f}{}'.format(cores['vermelho'], cores['fimcor'], cores['vermelho'], total, cores['fimcor'], cores['vermelho'], porcentagem, cores['fimcor']))
elif total <= porcentagem:
    print('Seu Financiamento {} FOI APROVADO{} pois,'
          '\no valor da parcela mensal de {}${:.2f}{} não excede 30% do Salário {}${:.2f}{}'.format(cores['azul'], cores['fimcor'], cores['azul'], total, cores['fimcor'], cores['azul'], porcentagem, cores['fimcor']))

