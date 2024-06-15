##variation in user defined function

#function with no argument no return value
def add():
    a=16
    b=20
    print(f'addition of {a} and {b} is :',a+b)
add()

#function with argument no return value
def add(a,b):
    print(f'addition of {a} and {b} is :',a+b)
a=10
b=20
add(a,b)

#function with no argument but return value
def add():
    a=10
    b=20
    return a+b
print(add())

#function with argument and return value
def add(a,b):
    return a+b
a=8
b=9
print(add(a,b))

## Types of argument

# positional argument fuction
def data(name,age,city):
    return f"my name is {name} my age is {age} and i live in {city}"

print(data(21,'Rohit',30))
print(data('Robert',20,'Thane'))

#Keyword argument function
def data(name,age,city):
    return f"my name is {name} my age is {age} and i live in {city}"

print(data(age=45,city='thane',name='Abc'))

# default argument function
def simple_int(p,r,t=7):
    print('principal is :',p)
    print('rate is :',r)
    print('time is :',t)

    si =p*r*t/100
    print('simple intereste is :',si)

p = 5000
r = 10
t = 5
simple_int(p,r)

#local variable
def display():
    a=10
    print(a)

display()

#Global variable
a=30
b=15
def display():
    a=20
    print(a)#20 second
print(b)#15 first
display()
print(a)#30 third

print()

a=30
def display():
    global a
    a=20
    print(a)#20
print(a)#30
display()
print(a)#20

a=10
y=5
def myfun():
    a=2
    y=a
    print(y,a)

myfun()
print(y,a)

b=30
def display(x):
    global a
    a=a+x
    return a
a=20
b=5
display(b)
print(a)


a=10
y=5
def myfun():
    global a
    y=a
    a=2
    print(y,a)
myfun()
print(y,a)

a=10
y=5
def myfun():
    global a
    a=2
    y=a
    print(y,a)
myfun()
print(y,a)
print()

# Modules and pakage
import math as m
print(m.sqrt(4))
print(m.factorial(5))
print(m.pow(2,3))
print(m.floor(15.9)) #round down number
print(m.ceil(15.2))  #round up number
print(m.floor(-15.9)) #round down number
print(m.ceil(-15.2))  #round up number

s = 'python_programming'
print(s[-15:-16]) #no output and no error
print(s[2:3:-1]) # no output and no error

import random as r
print(r.randrange(20))
print(r.randrange(2,8,2))
print(r.randrange(2))
#print(r.randrange(6,2)) gives error 

# to include both lower and higher value we can use randint but no step value
print(r.randint(6,6))
print(r.randint(2,8))
#print(r.randint(6,2)) gives error

#gives float value and there is no step
print(r.uniform(2,5))

#choose any data randomly from list
l=[11,22,33,44,'Robert']
print(r.choice(l))

# the list of data will be shuffled in every output
R=['Big_boss','sholey','karan_arjun']
r.shuffle(R)
print(R)









    



