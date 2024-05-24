name = "Robert"
age = 27
marks = 35.2

'''print("My name is %s and my age is %d and I earn %o.1f marks"%(name,age,marks))'''

'''print("My name is {} and my age is {} and I earn {} marks".format(name,age,marks))'''

print(f"My name is {name} and my age is {age} and I earn {marks} marks")


a = "My name is khan"
print(a[0])
print(a[-15])
s=""
for i in range(-1,-16,-1):
    s=s+a[i]
print(s)

s=""
for i in range(0,15,1):
    s=s+a[i]
print(s)

b= a[3:7:1]
print(b)

b= a[-12:-8:1]
print(b)

b= a[-1:-16:-1]
print(b)

print(a[::-1])

c = "hello Robert"
print(c.upper())

d="oral"
print(d.capitalize())

e= ("HELLO EVERYONE").lower()
print(e)

f=e.upper()
print(f)

    
    
