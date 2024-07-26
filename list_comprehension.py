#normal print
odd =[i for i in range(1,101,2)]
print(odd)

even =[i for i in range(2,101,2)]
print(even)

#to covert into uppercase
a = ['Robert','Anuj','abc']
print([i.upper() for i in a])

#one line code
print([i for i in a if 'b' in i])

#pick any name randomly
a = ['Robert','jenish','Robin','Venus','Arun','Vicky','Mari','Madhan']
import random
random = random.choice(a)
print(random)

