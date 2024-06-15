#basics in dictionary
a = {'name':'ABC',0:'kuch bhi','age':78,'name':'Robert'}
print(a)
b = a.copy()
print(b)
print(len(a))
print(type(a))

a['age'] = 20
a['city'] = 'tamilnadu'

print(a)

for i in a:
    print(f"{i} = {a[i]}")

#returns data in tuple
print(a.keys())
print(a.values())
print(a.items())

#Assign value
x = (1,2,3,4,5)
y = 0
print(dict.fromkeys(x,y))

#normal print
for k,v in a.items():
    print(k,':',v)

#added two list using for loop
keys = ['name','age','city']
values =['xyz',33,'thane']
data = {}
for i in range(0,len(keys),1):
    data[keys[i]] = values[i]
print(data)

#Methods in dictionary
a = {'name':'ABC',0:'kuch bhi','age':78}
print(a['name'])
print(a.get('name'))
print(a.get('age'))

a['phone'] = 7304795580
print(a)
a.update({'tel': 9137316635})
print(a)

a.pop('name')
print(a)
a.popitem()
print(a)
#a.clear()(to delete data)
#del a(to delete entire variable)
del a['age']
print(a)



