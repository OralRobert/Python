a = (1,2,3,'abc','xyz')
print(a)
print(type(a))
print(len(a))
print(a[-1])

#Added two tuple
b = (1,2)
print(a+b)
#to stor single value in tuple
s = (1,)
print(type(s))

#unpacked tuple
data = ('Robert',27,'Tamil_Nadu',23,234,43,34,24,34525,)
(name,age,city,*a) = data
print(city)
print(a[2])

#type casting
a = [1,2,3,([33,88,'abc',('yes','no','yes')])]
a[3][3] = ('yes','yes','yes')
print(a)

b = list(a[3][3])
b[1] = 'yes'
print(tuple(b))
a[3][3] = tuple(b)

print(a)

#to reverse the tuple
a = (1,2,3,44,5,6,6)
print(a[::-1])

#count a particular element
print(a.count(6))
#get a index value of particular element
print(a.index(5))

#normal print using loops 
a = (1,2,3,44,5,6,6)

for i in a:
    print(i)

i=0
while i<len(a):
    print (a[i])
    i+=1

for i in range(len(a)):
    print(a[i])

    



