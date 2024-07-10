##class is a blueprint that defines some properties and behaviors. An object
##is an instance of a class that has those properties and behaviors attached.
##A class is not allocated memory when it is created . Class is a logical entity
##whereas objects are physical entites.

class student:
    name = "Kaniyan"
    Roll_no = 76
    email_id = "kaniyan96@gmail.com"


s = student
print(s.name)
print(s.Roll_no)
print(s.email_id)
print(type(s.Roll_no))

class student:
    name = "manickam"
    Roll_no = 76
    email_id = "manickam96@gmail.com"

    def demo(self): #self is default parameter that represent instance of class
        name='Robertsdcs'
        print(name)


s = student()
s.demo()
print(s.name)

k = student()
k.demo()

m = student()
m.demo()


class A:
    def demo(self,department):
        print(department)
        print(self)
        name = 'Robert'
        age = 31
        roll_no = 123
        print(name,age,roll_no)

    def display(self):
        email = 'oralrobert96@gmail.com'
        address = 'Thane'
        print(email,address)

a=A()
a.demo('Mech')   # calling by object name
print(a)
a.display()
A.demo('k','Mech') # calling by class name 
a.demo('Mech')


class student:
    def show(self,name,roll_no):
        print('My name is',name)
        print('roll_no is',roll_no)
        print('I am a python developer')

    def display(self):
        print('java developer')

s=student()
s.show('Robert',123)
s.display()
print()
class student:
    name = 'Oral'
    email = "oralrobert96@gamil.com"
    def show(self):
        print(self.name,self.email)
        print('python developer')
    def display(self):
        print(self.name)
        print('java developer')

a = student()
print(a.name)
a.show()
a.display()
#
class A:
    def show(self,roll_no,dep_name):
        print(roll_no,dep_name)
        name = 'Robert'
        age = 27
        print(name,age)

    def display(self):
        #print(dep_name)
        email='oral@gmail.com'
        branch='Mumbai'
        #print(name)
        print(email,branch)
        
a = A()
a.show(123,'Mech')
#print(a.name)
a.display()


class A:
    def show(self,name,age,salary):
        a.n = name
        self.ag = age
        self.sal = salary
        print(a.n,self.ag,self.sal)
    def display(self):
        print(a.n,self.ag,self.sal)

a = A()
a.show('Robert',27,80000)
a.display()

class A:
    name = 'Rob'
    age = 19
    def show(self):
        print(a.name)
        print(a.age)


a = A()
a.show()

##class A:
##    def show(self):
##        self.name = input('Enter your name:')
##        self.age = int(input('Enter your age: '))
##        self.salary = int(input('Enter salary: '))
##    def display(self):
##        print('My name is ',self.name)
##        print('My age is ',self.age)
##        print('salary is',self.salary)
##
##a = A()
##a.show()
##a.display()


class A:
    def show(self,name,address):
        print('python developer')
    def display(self):
        self.show('saud','khan')
        a.show('kedar','itvedant')

        print('java developer')

a = A()
a.show('Robert','Thane')
a.display()

class A:
    a=10
    b=20

    def demo(s):
        s.a=s.a+1   # by calling object name
        A.b=A.b+1   #by calling class name
        print(s.a,A.b)

x = A()
x.demo()

y= A()
y.demo()

print() 
#constructors => __init__ method runs automatically when object is created
#which is used to initialize the instance object

class A:
    def __init__(s):
        print("krush")
        s.id=101
        s.name='kru'
        s.salary=25025

    def display(s):
        print('id is',s.id)
        print('name is',s.name)
        print('salary is ',s.salary)
        
a=A()    #consturctor runs automatically when object is created
a.display()


class A:
    def __init__(s):
        s.id=int(input('enter the id '))
        s.name=input('enter the name ')
        s.salary=int(input('enter the salary '))
    def display(s):
        print(f'id is {s.id}, name is {s.name} and salary is {s.salary}')
a=A( )

a.display()



class A:
    def __init__(s,name,age,salary):
        s.name=name
        s.age=age
        s.salary=salary
    def display(s):
        print(s.name,s.age,s.salary)
    def __str__(s):
        return s.name + " " + str(s.age) +" " + str(s.salary)
a=A('kru',23,151515)
a.display()
print(a)  #__str__ method runs when object gets printed

class A:
    def display(s,name,age):
        s.email='kru@gmail.com'
        print(name,age,s.email)
        print('python dev')

    def show(s):
        print(s.email)
        s.display('KJ',22)
        print('java dev')

    def demo(k):
        print(k.email)
        print(a.email)

a=A()
a.display('kru',211)
a.show()
a.demo()

##destructor => is a member method of calss it delete the memory of object
##it can b called with object :-  __del__

##garbage collector:
##a progra, to delete reference
##it runs automatically
##it does mamory management

class A:
    def __init__(j):
        j.name='KJ'
        print('python debv')
    def show(k):
        print("java dev")
    def __del__(k):
        print("Object deleted ")
a=A()
a.show()
del a
#a.show()  # it will not execute coz objejct a deleted by destructor method





        












