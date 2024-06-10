# positional argument fuction
def data(name,age,city):
    return f"my name is {name} my age is {age} and i live in {city}"

print(data(21,'Rohit',30))
print(data('Robert',20,'Thane'))

#Key word argument function
def data(name,age,city):
    return f"my name is {name} my age is {age} and i live in {city}"

print(data(age=45,city='thane',name='Abc'))

##variation in user defined function

#function with no argument no return value
def add():
    a=10
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

