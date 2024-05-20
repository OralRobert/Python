type1 = input("which type of food you are looking for veg/non-veg :" )

if type1 == 'veg':
    print("\n1. paneer tikka \n2. dal rice \n3. veg biryani")
    food = input("Which food you like to have :")
    if food == 'paneer tikka':
        print("\n1. Rate:300 \n2. butter roti : 4")
    elif food == 'dal rice':
        print("\n1. Rate:100 \n2. papad :1 \n3. onion : 5 slices") 
    elif food == 'veg biryani':
        print("\n1. Rate : 150 full /90 half \n2. onion : 5 slices")
    else:
        print("here that food is not available")
elif type1 == 'non-veg':
    print("\n1. chiken-Biryani \n2. Mutton-Biryani \n3. Crab-Masala")
    food = input("which food you like to have :")
    if food == 'chiken-Biryani':
        print("\n1. Rate : 150 full/90 half \n2. side-dish : onion raita")
    elif food == 'Mutton-Biryani':
        print("\n1. Rate : 250 full /150 half \n2. side dish : onion raita,5 slice of onion") 
    elif food == 'Crab-Masala':
        print("\n1. Rate : 250 full/180 half \n2. Butter roti : 4")
    else:
        print("here that food is not available")
        
    
