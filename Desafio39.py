from datetime import date
ano = int(input('Digite o Ano de Nascimento: '))
atual = date.today().year
sub_ano = atual - ano
print ('Você tem: {} de Idade em {}'.format(sub_ano, atual))


if sub_ano == 18:
    print('Você esta em fase de Alistamento Militar')
elif sub_ano < 18:
    menor_idade = 18 - sub_ano
    print('Faltam {} anos para o Serviço Militar'.format(menor_idade))
elif sub_ano > 18:
    velho = sub_ano - 18
    print('Você passou {} do seu Alistamento, Estamos te procurando!'.format(velho))