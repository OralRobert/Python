a = [1,2,3,'abc','xyz']
a.append("Added")
print(a)

a = [1,2]
b = [3,4]
a.extend(b)
print(a)
b.extend(a)
print(b)


a = [1,2,3,4]
a.insert(0,100)
a.insert(0,100)
a.insert(2,300)
a.insert(2,400)
print(a)

a = ['abc',100,200]
a[1] = 'robert'
print(a)

a = [1,2,3,4,5]
a.pop()
print(a)
a.remove(1)
print(a)

a=[1,2,3,4,5]
del a[0]
print(a)

ab =[1,2,3,4,4,4]
print(ab.count(4))

print(ab.index(4))
ab.reverse()
print(ab)


a=[1,2,3,4,5,6,7,8]
a.clear()
print(a)
