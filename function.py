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
print(add(20,30))
print(add(10,60))

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

# Arbitary argument(variable length parameter) #*args #**kwargs
def simple(*args):
    for i in args:
        print(i*3)
simple(2,3,4,5,6)

def data(**kwargs):
    for i,j in kwargs.items():
        print(i,":",j)
data(name = "Robert",age = 27,Roll_no = 76)
    
print()
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



print()
###lambda function: a function without name is called as lambda function.
##it is also called anonymous function.lamda function always start with lambda
##keyword
#sytex
#lambda argument:expression

a = lambda x:print(x**2)
a(4)

a = lambda x:x**2
print(a(4))

add = lambda x,y:print(x+y)
add(3,4)

add = lambda x,y:x+y
print(add(3,4))

result = lambda x,y:(x+y,x-y)
print(result(3,4))
add,sub = result(3,4)
print(add)
print(sub)

add = lambda x,y=5:x+y
print(add(3))

add = lambda x=3,y=5:x+y
print(add())

sub = lambda y,x:x-y
print(sub(x=3,y=9))

#Higher order function
#Built in higher order function
#1. Filter function

number = [11,22,33,44,55,66]
def even_fun(x):
    if x%2==0:
        return True
filter_object = filter(even_fun,number)
print(filter_object)
print(list(filter_object))
print(list(filter_object))


number = [11,22,33,44,55,66]
def even_fun(x):
    if x%2==0:
        return True
filter_object = list(filter(even_fun,number))
print(filter_object)



b = [2,3,4,5,6,7,8,9,23]
def prime_fun(y):
    for i in range(2,y,1):
        if y%i==0:
            return False
    else:
        return True
filter_ = list(filter(prime_fun,b))
print(filter_)

#2. Map function

n= [1,2,3,4,5,6]
def square(x):
    return x*x

y=list(map(square,n))
print(y)

#
a = [3,4,5,6]

def fac(b):
    for i in range(1,b):
        b = i*b
    return b

fil = list(map(fac,a))
print(fil)



#
def A(x,y):
    c=x+y
    def B(d):
        print(d+1)
    return B(c)
print(A(2,3))
print()

#
def A(x,y):
    return x+y
B=A
print(B(2,3))
print()

#
def A(n):
    if (n>5):
        return 1
    return 2
x = A(2)+A(10)
print(10)
print()
#
def A():
    pass
print(A())
print()
#
def A(x,y):
    print(x+y)
print(A(2,3))
print()
#
def A(x,y):
    print(x+y)
B = A
B(2,3)
print()
#
def A(x,y):
    return x+y
B = A
B(2,3)
print()
#
def A(n):
    if (n > 5):
        return 1
    else:
        return 2
    return
print(A(5))
print()
#
def A(n):
    for i in range(1,11):
        return n*i
    return n
print(A(2))

##a = open('oral','w+')
##print(a)


