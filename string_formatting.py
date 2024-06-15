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

s = 'python_programming'
print(s[-15:-16]) #no output and no error
print(s[2:3:-1]) #no output and no error

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

g = "Hi How are You"
print(g.title())

print(g.swapcase())

#it will check the data is in alphabet,the output will beT/F 
h = "hdfbjhd"
print(h.isalnum())

#it will check the data is in alphabet but lower case,the output will beT/F 
i = "hkbcjhSDbc"
print(i.isalpha())

#it will check the data is in int,the output will beT/F 
j = "132323423"
print(j.isdigit())

#Methods to check weather the data is lower or upper case
##print(isupper())
##print(islower())

# replaceses the word we wanted
k = "Python is low level language"
l = k.replace('low','high')
print(l)

#splits in given place and put data into list
m = "python-java-php-.net"
n = m.split('-')
print(n)

date = '2022/06/12'
o = date.split('/')
print(o)

#gives only value assingned to index
p="Robert"
for i in p:
    print(i)

#gives only index value
for i in range(len(p)):
    print(i)
    
