# creating list with constructor method

a = list((1,2,'abc','xyz'))
print(a)
print(type(a))
print(len(a))


#list
b = [1,2,'abc','xyz']
print(b)
print(type(b))
print(len(b))


# print a particular word which contains the given letter
#last letter(i)
c=['robert','anuj','mishraji','saud','jadhav','nair']
for i in c:
    if i[-1]=='i':
        print(i)

#r
for i in c:
    if 'r' in i:
        print(i)

#r 
for i in c:
    for j in i:
        if j=='r':
            print(i)
            break


d = ['Robert','anuj','mishraji','jadhav','nair','more','jagtap','ingle']

i=0
while i<len(d):
    j=0
    while j<len(d[i]):
        if d[i][j]=='r':
            print(d[i])
            break
        j+=1
    i+=1
d = ['Robert','anuj','mishraji','jadhav','nair','more','jagtap','ingle']
i=0
while i<len(d):
    j=0
    e=0
    while j<len(d[i]):
        if d[i][j] in 'aeiou':
            e=e+1
        j+=1
    print(f"{d[i]} this name contains{e} vowels")
    i+=1
    
d = ['Robert','anuj','mishraji','jadhav','nair','more','jagtap','ingle']
for i in d:
    count=0
    for j in i:
        if j in 'aeiou':
            count+=1
    print(i,count)

d = ['Robert','anuj','mishraji','jadhav','nair','more','jagtap','ingle']
for i in d:
    count=" "
    for j in i:
        if j in 'aeiou':
            count=count+j
    print(f"{i} this name contains {len(i)} letters {len(count)} vowels and the vowels are {count}")    
            
# separated even and odd no in two separate list
a=[1,2,3,4,5,6,7,8,9,10]
e = []
o = []

for i in a:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print(e)
print(o)

#separate duplicate no. to another list
a = [1,2,3,4,5,6,7,7,7,6,6,6,4]
b = []
c1 = []
for i in a:
    if i not in b:
        b.append(i)
    else:
        c1.append(i)
print(b)
print(c1)

# find no.of duplicates
for i in b:
    c2 =0
    for j in c1:
        if j == i:
            c2 = c2+1
    if c2:
        print(f" {i} duplicates are {c2}")
        
#normal print
a = [[['Robert','anuj','mishraji','jadhav','nair','more','jagtap','ingle']]]
for i in a:
    for j in i:
        for x in j:
            print(x)

#normal print
b = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for i in b:
     for j in i:
         print(j)
         
l = [['e'],['l'],['e'],['p'],['h'],['a'],['n'],['t']]
i = 0
while i<8:
    print('i',i+1)
    for j in l[i]:
        print('{}'.format(j),end='')
    break
print()

##l = [['e'], ['l'], ['e'], ['p'], ['h'], ['a'], ['n'], ['t']]
##i = 0
##
##while i < 8:
##    print('i', i+1)
##    for j in l[i]:  # Corrected syntax: access element using l[i] instead of l(i)
##        print('{}'.format(j), end='')
##    print()  # Print a newline after printing each sublist
##    i += 1  # Increment i to avoid an infinite loop

a = [[['Robert','anuj','mishraji','jadhav','nair','more','jagtap','ingle']]]
for i in a:
    for j in i:
        print(j[0])
    
