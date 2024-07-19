#current date - datetime.now()
#Today date - date.today()
#classes
##1. Date class - Helps to deal with individualunit of date
##2. Time class - Helps to deal with individual unit of time
##3. Datetime class - Helps to deal with date & time all files
##4. TimeDelta - object represents the differencd two dates or times
##5. strftime() - used to format datetime fields representation
import datetime

dt = datetime.datetime.now()# return current system date and time
print(dt,type(dt))

dt1 = datetime.datetime(2023,3,1,12,50,30,29)# it will type cast into date time
print(dt1)
print(dt1.hour)
print(dt1.minute)
print(dt1.second)
print(dt1.microsecond)

date = datetime.date.today()# print today's date
print(date)
print(date.month)
print(date.year)
print(date.day)

date_after_2days = dt+datetime.timedelta(days=2)
print(date_after_2days)

date_after_2days_3weeks = dt+datetime.timedelta(days=2,weeks=3)
print(date_after_2days_3weeks)

#strftime: it is used to represent date and time in string format
#%a: sun,mon,tue
#%A: sunday,Monday
#%d: print month indigits 1,2,3..12
#%b: jan,feb...
#%B: January...
#%y: last two digit of year 23,24,25...
#%Y: 2023,2024...

s = dt.strftime("%a %d %y")
print(s)

s1 = dt.strftime("%A %D %Y %b %H:%M:%S")
print(s1)

# Modules and pakage
import math as m
print(m.sqrt(4))
print(m.factorial(5))
print(m.pow(2,3))
print(m.floor(15.9)) #round down number
print(m.ceil(15.2))  #round up number
print(m.floor(-15.9)) #round down number
print(m.ceil(-15.2))  #round up number

s = 'python_programming'
print(s[-15:-16]) #no output and no error
print(s[2:3:-1]) # no output and no error

import random as r
print(r.randrange(20))
print(r.randrange(2,8,2))
print(r.randrange(2))
#print(r.randrange(6,2)) gives error 

# to include both lower and higher value we can use randint but no step value
print(r.randint(6,6))
print(r.randint(2,8))
#print(r.randint(6,2)) gives error

#gives float value and there is no step
print(r.uniform(2,5))

#choose any data randomly from list
l=[11,22,33,44,'Robert']
print(r.choice(l))

# the list of data will be shuffled in every output
R=['Big_boss','sholey','karan_arjun']
r.shuffle(R)
print(R)
