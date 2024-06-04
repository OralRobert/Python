a = ['Robert','jenish','Robin','Venus','Arun','Vicky','Mari','Madhan']
import random
print(random.choice(a))
print(random.choices(a,k=3))
print(random.sample(a,k=2))
random.shuffle(a)
print(a)
print(random.randint(1,10))
print("".join(random.sample('1234567890',k=4)))
