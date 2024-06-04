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



        



        
        
