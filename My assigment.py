###Write a program that accepts a string from the user
##and display the same string after removing vowels from it.
user = input("enter your string:")
j = "aeiou"
r = ""
for i in user:
    if i not in j:
        r+=i

print(r)    
