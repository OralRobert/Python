# positional argument fuction
def data(name,age,city):
    return f"my name is {name} my age is {age} and i live in {city}"

print(data(21,'Rohit',30))
print(data('Robert',20,'Thane'))

#Key word argument function
def data(name,age,city):
    return f"my name is {name} my age is {age} and i live in {city}"

print(data(age=45,city='thane',name='Abc'))
