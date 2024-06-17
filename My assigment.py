###Write a program that accepts a string from the user
##and display the same string after removing vowels from it.
user = input("enter your string:")
j = "aeiou"
r = ""
for i in user:
    if i not in j:
        r+=i

print(r)

##Write a program that creates a list of 10 random integers.Then create two
##lists by name odd_list and even_list that have all odd and even values of
##the list respectively.
import random
i = [random.randint(1,100)for i in range(10)]
print("random list",i)
e = []
o = []
for j in i:
    if j%2==0:
        e.append(j)
    else:
        o.append(j)

print("even no. in list",e)
print("odd no. in list",o)

