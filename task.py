#1.take input from user and print its inputvalue using input function
##user = input("Enter your name : ")
##print("Hello",user)

#2 create a string and print the last element
a = "Robert"
print(a[-1])

#3 create a string and print second last element
b = "Robert"
print(b[-2])

#4 create a string hello and print multiple times
a = "Hello"
print(a*5)

#5 create two string like hello and world and print  "helloworld"
a = "hello"
b = "world"
print(a+b)

#Print your name 10 times without using loop and manually
a = " Robert "
print(a*10)

#WAP for Factorial 
n = 5
f = 1

for i in range(1,n+1):
    f*=i

print(f)

#Wap for factorial using recurssion
def f(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * f(n-1)

n = 5
print(f(n))

# Find pow of n using recurssion
def pow(n,p):
    if p==0:
        return 1
    else:
        return pow(n,p-1)

print(pow(2,3))

#6.create two variable and swap its value ex a=10,b=20 after swapping a=20,b=10
a=20
b=10

y = a 
a = b
b = y
print(a,b)

#7. create a tuple like(1,2,3,4,3,2) and count number of ocurrences of 3
a = (1,2,3,4,3,2,3)
count = 0
for i in a:
    if i==3:
        count+=1
print(count)

#8. cretae a tuple like(1,2,3,4,3,2) and print the index number of 3
a = (1,2,3,4,3,2)
for i in a:
    if i == 3:
        print(a.index(i))

#9. create a tuple like (1,2,3,4,3,2) and print the (2,3,4)only
a = (1,2,3,4,3,2)
print((a[1],a[2],a[3]))

#10. create a tuple like (1,2,3,4,3,2) and remove 3 in this tuple
a = (1,2,3,4,3,2)
b = list(a)
print(b)
for i in b:
    if i==3:
        b.remove(i)

print(tuple(b))

#11. create a list [1,2,3,4] and change the elements in like [1,2,4,3] without
#using list methods
a = [1,2,3,4]
a[2],a[3] = a[3],a[2]
print(a)

#create a list [1,2,3,4] and change the elements in like [1,2,4,3] with
#using list methods
a = [1,2,3,4]
a.pop(2)
print(a)
a.insert(4,3)
print(a)

#12.create a list like [1,2,3,4] and delete all the elements in list and print
#empty list without using any mehtod
a = [1,2,3,4]
while a:
    a.pop()

print(a)

#13.create single value tuple
a = (17,)
print(type(a))

#14. create empty set
a = {}
a = set()
print(type(a))

#15. create a dictionary like {"a":10,"b":20} and print the value of "a" without
#using methods
a = {"a":10,"b":20}
print(a["a"])

#16. create a dictionary like {"a":10,"b":20} and change the value of "b" is 30
#and print it without using methods
a = {"a":10,"b":20}
b = {"a":10,"b":20,"b":30}

b["a"] =  40
print(b)
print(b)
print(a)

#17. create a dictionary like{"a":10,"b":20} and insert the key value pair
#which the key is "c" and the value is 30 and print it
a = {"a":10,"b":20}
a["c"] = 30
print(a)

#18 create two sets like {1,2,3,4} and {3,4,5,6} and find the union without
#using union method
a = {1,2,3,4}
b = {3,4,5,6}
c = a.copy()
print(c)
for i in b:
    if i not in a:
        a.add(i)
print(a)

#20 create two sets like{1,2,3,4} and {3,4,5,6} and find ther difference without
#using difference method
a = {1,2,3,4,9}
b = {3,4,5,6}
c = set()
for i in a:
    if i not in b:
        c.add(i)
print(c)

#21 create a set like {1,2,3,4} and remove 3
a = {1,2,3,4}
a.remove(3)
print(a)
