nome = str(input('Insert Your Full Name: ')).strip()

print('Analizando seu Nome...')

print("Seu nome em Maiúsculas é: {}.".format(nome.upper()))

print("Seu nome em Minúsculas é: {}.".format(nome.lower()))

print("Seu Nome tem ao todo tem {} Letras".format(len(nome) - nome.count(' '))) #nome.count(' ') comprimento do nome menos o spaço

print('Seu primeiro nome tem {} letas.'.format(nome.find(' '))) #nome.find(' ') find the first space

print('Test...')

separa = nome.split()
print("Seu primeiro nome é {} e tem o {} Letras.".format(separa[0], len(separa[0])))