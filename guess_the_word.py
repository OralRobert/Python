import random
words = ['robert','berort','mishraji','mijirash','rajit','arjit',
         'krushna','rushank','tanaya','yatana','dhashra','namita','manita',
         'netra','terna','ashish','shisha','abhishek','vishal','shalvi']
score = 0
while True:
    cwords = list(random.choice(words))
    print("your given word","".join(cwords))
    user_word = input("enter your answer : ")
    if user_word == "quit":
        break

    for letter in user_word:
        if letter in cwords:
            cwords.remove(letter)
            valid = True

        else:
            valid = False
            

    if valid and user_word in words:
        score = score + len(user_word)
        print(f"correct your score is {score}")
    else:
        print("your answer is wrong")
print("Thank you so much")


        

    
    