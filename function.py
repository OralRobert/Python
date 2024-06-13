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



    



