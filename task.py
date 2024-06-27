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
#a = {}
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

#22 create a set like {1,2,3,4} and remove 3 using discard method and understand
#what's the difference between remove and pop
a = {1,2,3,4}
a.discard(3)
print(a)
a.pop()
print(a)

#23. create a string like "hello world" and count "o"
a = "hello world"
b = a.count("o")
print(b)
c = a.index("o")
print(c)

#24. create a string like "hello world" and find "z" or index "z" and understand
#difference between index and count
a = "hello world"
for i in a:
    if i == "z":
        print(f"z found")
    else:
        print(f"z not found in {i}")

#25. create a list like ["p","y","t","h","o","n"] and print "python"
a = ["p","y","t","h","o","n"]
b = "".join(a)
print(b)

#26.create a string "pyhton" and print ["p","y","t","h","o","n"]
a = "python"
b = list(a)
print(b)

#27. create a string like "     python" and print "python"
a = "     pyhton"
b = a.strip()
print(b)

#28. create a list [1,2,3,4] and print it like [1,2,3,4,5]
a = [1,2,3,4]
a.append(5)
print(a)

#29. create a list [1,2,3,4] and print[1,2,3,4,1,2,3,4]
a = [1,2,3,4]
b = [1,2,3,4]
a.extend(b)
print(a)

#30. create a list [1,2,3,4] and print [1,2,3,4,"p","y","t","h","o","n"]
a = [1,2,3,4]
b = ["p","y","t","h","o","n"]
a.extend(b)
print(a)

#31. create a list [1,2,3,4] and remove 2 using pop function
a = [1,2,3,4]
a.pop(1)
print(a)

#32. create a list [1,2,3,4] and print [1,5,3,4] using insert function
a = [1,2,3,4]
a.insert(1,5)
print(a)

#33. create a list [1,2,3,4] and print[1,5,3,4] using negative indexing in insert
#function.
a = [1,2,3,4]
a.insert(-3,5)
print(a)

#34. create a list [1,2,3,4] and print[4,3,2,1]
a = [1,2,3,4]
a.reverse()
print(a)

#35. create a list [1,4,3,2] and print[1,2,3,4] using function
a = [1,4,3,2]
a.sort()
print(a)

#36. create a dict{"a":10,"b":12,"c":14} and clear it{}
a = {"a":10,"b":12,"c":14}
a.clear()
print(a)

#37. create a empty set{}
a = set()
print(a)

#38. create a empty dict
a = {}
print(a)

#39. create a dict{"a":10,"b":20,"c":30} and print {"b":20,"c":30}
a = {"a":10,"b":20,"c":30}
a.pop("a")
print(a)

#40. create a set {1,2,3,4} and remove 2
a = {1,2,3,4}
a.remove(2)
print(a)

#moderate question

#1. create a string "hello" and print >> ll:2 times without using count method
a = "hello"
b = 0
for i in a:
    if i == "l":
        c = ''.join(i)
        b+=1
print(f"{c}:{b}")

#2. create a string "hello" and sort it
a = "hello"
b = ''.join(sorted(a))
print(b)

#3. Take input string from user and find vowels
'''a = input("user input : ")
for i in a:
    if i in "aeiou":
        print(i)'''

#4. create a list [(1,2),{"a":10},"abv",[1,2,3,4]] and find the data type of
#each element

a = [(1,2),{"a":10},"abv",[1,2,3,4]]
print(type(a[0]))
print(type(a[1]))
print(type(a[2]))
print(type(a[3]))

#5. print A to Z in sequence like A B C D E...........XYZ
for i in range(ord('a'),ord('z'),+1):
    print(chr(i),end=" ")

#6. print ten time "hii"
print()
a = " hii "
print(a * 10)

#7. print right angle triangle using while loop
i=5
while i<=5:
    print('*',end='')
    i-=1
    print()
    break

for i in range(100,201,1):
    if i%2==0:
        print(i)










                   






        


