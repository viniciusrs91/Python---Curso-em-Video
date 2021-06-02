#Escreva um programa que pergunte a quantidade 
# de Km percorridos por um carro alugado e a
#  quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro 
# custa R$60 por dia e R$0,15 por Km rodado.

d = int(input('How many days with car? '))
km = float(input('How many Miles runned? '))

t = (d*60) +(km * 0.15)

print ('Your total is: ${}'.format(t))