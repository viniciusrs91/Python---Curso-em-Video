from datetime import date
# è ano bissexto?
a = int(input("Digite o Ano para Analizar: "))
if a == 0:
    a = date.today().year
elif a % 400 == 0:
    print('{} É ano Bissexto'.format(a))
elif a % 4 == 0 and a % 100 != 0:
    print('{} É ano Bissexto'.format(a))
else:
    print('{} Não é Ano Bissexto.'.format(a))


