import random

n1 = input("Studant name 1: ")
n2 = input("Studant name 2: ")
n3 = input("Studant name 3: ")
n4 = input("Studant name 4: ")

r = random.choices([n1,n2,n3,n4,])
#print (r)
print ("The selected Studant to clean up the blackboard is: {}".format(r))

#list in python we declare with [n1,n2,n3,n4]
