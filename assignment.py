
sets = 3
pr = []
no = []
Ra = []

for i in range(sets):
    P = float(input("enter your principal : " ))
    N = float(input("enter your no of year : " ))
    R = float(input("enter your Rate of interest : " ))

    pr.append(P)
    no.append(N)
    Ra.append(R)
    
for i in range(sets):
    Total = (pr[i]*no[i]*Ra[i])/100
    print(Total)

