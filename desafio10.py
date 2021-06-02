# Money Converter

r= float(input('Insert Your Money R$:'))
dhj = float(input('Insert Dolar Today $:'))
#d= float(r//dhj) inteiro
d= float(r/dhj) 
print ('With R${:.2f} You can Buy ${:.2f} Dolars. \nThank You.'.format(r,d))
