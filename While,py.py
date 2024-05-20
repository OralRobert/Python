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
    
    












    
    
