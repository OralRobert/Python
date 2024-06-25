for i in range(1,11,1):
    print(i)
    
# to find prime no. or not
n=17
for i in range(2,n,1):
    if n%i==0:
        print(n,"not an prime no")
        break
else:
    print(n,"is an prime no")


#prime n0. 1 to 100
for n in range(2,101,1):
        for j in range(2,n,1):
            if n%j==0:
                break
        else:
            print(n)



'''for j in range(2,101):
    for i in range(2,j-1):
        if j%i==0:
            break
    else:
        print(j,"is an prime no")'''


#task
for i in range(1,11):  
    pass
print(i)

#
i = 20
for i in range(1,11): 
    pass
print(i)
print()
#
for i in range(1,4): 
    print(i)   #1,1,1
    print(i)   #2,2,2
    print(i)   #3,3,3
print(i)       #3
print()
#
for i in range(1,4):
    print(i)      #1,2,3
    print(i+1)    #2,3,4
    print(i+2)    #3,4,5
print(i)          #3

#
for i in range(1,4):
    print(i)     #1,2,3
    i=i+1

#
for i in range(1,4):
    i=i+1
    print(i) #2,3,4

print()
#
for i in range(1,4):
    for j in range(1,4):
        print(i,j)   #1[1,2,3]/2[1,2,3]/3[1,2,3]
print()
#
for i in range(1,4):
    print(i)        #1,2,3
    for j in range(1,4):
        print(i,j)  #1[1,2,3]/2[1,2,3]/3[1,2,3]
    print(j)        #3,3,3
print(i,j)          #3,3

#
for i in range(1,4):
    print(i)     #1,2,3
    if (i==2):
        continue
print(i)      #3



        



        
        
