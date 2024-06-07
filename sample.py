#Example for break
book = ("java",".net","python","c++","php")
for i in book:
    if i == "python":
        print("found book : ",i)
        break
    else:
        print("searching")

#Example for continue
book = ("java",".net","python","c++","php")
for i in book:
    if i == "python":
        continue
    print(i)

# even
for i in range(100,201,1):
    if i%2==0:
        print(i)

#assignemnt
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

#assignemnt
P = int(input("enter your value : " ))
N = int(input("enter your value : " ))
R = int(input("enter your value : " ))
print((P*N*R)/100)

    

