a = {'aa','xyz','pqr'}
a.add('rohit')
a.update({'Robert','Roshan'})
print(a)
a.pop()
print(a)

for i in a:
    print(i)

#to generate otp
b = {'0','1','2','3','4','5','6','7','8','9'}
c = ""
for i in b:
    c = c+i
print(c[:4:])

s2={1,4,2,5,7,8,9.10,55,50,70,80,10,50,10,30,"abc"}
print(s2)
s2.add(777)
print("add : ",s2)
s2.update(('a','b','c'))
print("update : ",s2)
s2.pop()
print("pop : ",s2)
s2.remove("abc")
print("remove : ",s2)
s2.discard("abcde")
print("discard: ",s2)
s2.clear()
print(s2)

#union & intersection
s1={10,20,30,40}
s2={30,40,50,60}
#result=s1.union(s2)
result=s1|s2
print(result)
#r1=s1.intersection(s2)
r1=s1&s2
print(r1)

