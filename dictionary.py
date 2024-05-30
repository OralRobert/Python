#basics in dictionary
a = {'name':'ABC',0:'kuch bhi','age':78,'name':'7328371273'}
print(a)
print(len(a))
print(type(a))

a['age'] = 20
a['city'] = 'tamilnadu'

print(a)

for i in a:
    print(f"{i} = {a[i]}")

#added two list using for loop
keys = ['name','age','city']
values =['xyz',33,'thane']
data = {}
for i in range(0,len(keys),1):
    data[keys[i]] = values[i]
print(data)
