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


##Write a program that has the dictionary of your friends’ names as keys and phone
##numbers as its values. Print the dictionary in a sorted order. Prompt the user to
##enter the name and check if it is present in the dictionary. If the name is not present,

#then enter the details in the dictionary.
my_dict = {'jenish':'7304795581','robin':'7304795582','venus':'7304795583',
           'adhithya':'7304795584'}
print(sorted(my_dict.items()))
name = input('enter name : ')
no = int(input('enter no. : '))
if name in my_dict:
    print('Name is already present in my dict')
else:
    my_dict[name] = no

print(my_dict)

for i in range(100,201,1):
    if i%2==0:
        print(i)

# write a program that receives 3 sets of values
# of p, n, and r and calculates simple interest for each
sets = 3
pr = []
no = []
Ra = []

for i in range(sets):
    P = float(input("enter your principal : " ))
    N = float(input("enter your no of year : " ))
    R = float(input("enter your Rate of interest : " ))

    pr.append(P)
    no.append(N)
    Ra.append(R)
    
for i in range(sets):
    Total = (pr[i]*no[i]*Ra[i])/100
    print(Total)

