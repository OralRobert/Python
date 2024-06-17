import random
i = [random.randint(1,100)for i in range(10)]
print("random list",i)
e = []
o = []
for j in i:
    if j%2==0:
        e.append(j)
    else:
        o.append(j)

print("even no. in list",e)
print("odd no. in list",o)
