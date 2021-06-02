#Inset a number and get double, triple 
# and root square

n = int(input ('Enter a Number: ') )
n2 = n*2
n3 = n*3
nr = n**(1/2) #Raiz quadrada pow(n,(1/2))

print ('The number is {}, the double is {}, the triple is {}, the square root is {:.2f}.'.format (n, n2,n3,nr))