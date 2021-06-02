import random

n1 = str(input("Studant name 1: "))
n2 = str(input("Studant name 2: "))
n3 = str(input("Studant name 3: "))
n4 = str(input("Studant name 4: "))

list = [n1,n2,n3,n4]

random.shuffle(list)

print ("The sequence to presentation is: ")
print (list)

