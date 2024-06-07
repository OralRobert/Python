a = {'aa','xyz','pqr'}
a.add('rohit')
a.update({'Robert','Roshan'})
print(a)
a.pop()
print(a)

for i in a:
    print(i)

b = {'0','1','2','3','4','5','6','7','8','9'}
c = ""
for i in b:
    c = c+i
print(c[:4:])
