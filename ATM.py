amount = 3850

if amount%50==0:
    if amount >= 500:
        print(amount)
        notes = amount//500 
        print("500 rs notes are",notes)
        amount = amount %500
    if amount >= 200:
        notes = amount//200
        print("200 rs notes are",notes)
        amount = amount%200
    if amount >= 100:
        notes = amount//100
        print("100 rs notes are",notes)
        amount = amount%100
    if amount >= 50:
        notes = amount//50
        print("50 rs notes are",notes)
    
else:
    print("Amount should be multiple of 50")