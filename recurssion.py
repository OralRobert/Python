##recurssion: when a function call itself ,then that function is called as
##recursive function and the process is called as recursion

##def demo():
##    print('rajesh')
##    demo()
##
##demo()

##i=0
##def demo():
##    global i
##    i+=1
##    print('Robert',i)
##    demo()
##demo()

##import sys
##print(sys.getrecursionlimit())
##sys.setrecursionlimit(200)
##print(sys.getrecursionlimit())
##
##i=0
##def demo():
##    global i
##    i=i+1
##    print('Robert',i)
##    demo()
##
##demo()


#Advantage:
#1) Clean code/less number of code   
#2) Complex promblem can

#Disadvantage
#1) Hard to debug
#2) not memory efficientbe solved

#WAP for fibbonacci series using recursion
##0,1,1,2,3,5,8,13,21,34,55.........
##fibo(1)=0
##fibo(2)=1
##fibo(3)=fibo(1)+fibo(2)
##fibo(3)=fibo(3-2)+fibo(3-1)
##fibo(n)=fibo(n-2)+fibo(n-1)

def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibo(n-2)+fibo(n-1)

n=int(input('enter the number of terms: '))
print(fibo(n))

#find prime no using recurssion
#wap for a counting no. of digit by using recurssion
#sum of first n no. using recurssion
#wap for printing n to 1 sequence
#wap for factorial using recurssion
