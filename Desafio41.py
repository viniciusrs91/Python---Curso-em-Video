from datetime import date
ano = int(input('Ano de Nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano

if idade <= 9:
    print('Com a idade de {} anos. MIRIM'.format(idade))
elif idade > 9 and idade <=14:
    print('Com a idade de {} anos. INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('Com a idade de {} anos. JUNIOR'.format(idade))
elif idade == 20:
    print('Com a idade de {} anos. SÊNIOR'.format(idade))
else:
    print('Com a idade de {}. MASTER'.format(idade))
