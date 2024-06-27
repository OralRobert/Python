
i=1
while i<=10:
    print(i)
    i+=1

n = 153
n1 = n
arm = 0
l = len(str(n))
while n!=0:
    rem = n%10
    arm = arm+rem**l
    n = n//10
if n1 == arm:
    print("This is an Armstrong number")
else:
    print("Not A Armstrong number")


row=1
while row<=5:
    col=1
    while col<=5:
        if row==1:
            print("A",end=" ")
        elif col==1:
            print("C",end=" ")
        elif row==col:
            print("B",end=" ")
        else:
            print(" ",end=" ")
        col=col+1
    row+=1
    print()

#print(ord('a'))
row=97
while row<=101:
    col=97
    while col<=row:
        print(chr(row),end=" ")
        col+=1
    row+=1
    print()

col=97
while col<=101:
    row=97
    while row<=col:
        print(col,end=" ")
        row+=1
    col+=1
    print()

row=97
i=1
while row<=101:
    cols = 1
    while cols<=5-i:
        print(" ",end=" ")
        cols+=1
    col=97
    while col<=row:
        print((row),end=" ")
        col+=1
    i+=1
    row+=1
    print()


n=23
i=2
while i<=17:
    if n%i==0:
            print(n,"is not a prime no")
            break
    else:
        print(n,"is a prime no")
        break
        
            
    
        
            
'''row=111
while row<=111:
    col = 111
    while col<=row:
        if row==col:
            print(row,end=" ")
        else:
            print(" ",end=" ")
            col-=1
        row-=1
        print()'''

# Normal print
a = [[['Robert','anuj','mishraji','jadhav','nair','more','jagtap','ingle']]]
i = 0
while i<len(a[0][0]):
    print(a[0][0][i])
    i+=1


b = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
i = 0
while i<len(b):
    j = 0
    while j<len(b[i]):
                print(b[i][j])
                j+=1
    i+=1
    
#task     
x=1
while (x<11):
    x=x+1
    break
print(x)

x=1
while (x<11):
    x=x+1
    pass
print(x)

x = 0
while(x<11):
    print(x)
    x=x+1
    if (x==5):
        continue

x=0
while (x<11):
    x=x+1
    if(x==5):
        break
    print(x)





    
             
             
    
     
            
            
        
        
        
    
    












    
    
