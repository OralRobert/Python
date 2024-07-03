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











