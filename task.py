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

