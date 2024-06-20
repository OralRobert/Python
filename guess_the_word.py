##import random
##words = ['robert','berort','mishraji','mijirash','rajit','arjit',
##         'krushna','rushank','tanaya','yatana','dhashra','namita','manita',
##         'netra','terna','ashish','shisha','abhishek','vishal','shalvi']
##score = 0
##while True:
##    cwords = list(random.choice(words))
##    print("your given word","".join(cwords))
##    user_word = input("enter your answer : ")
##    if user_word == "quit":
##        break
##
##    for letter in user_word:
##        if letter in cwords:
##            cwords.remove(letter)
##            valid = True
##
##        else:
##            valid = False
##            
##
##    if valid and user_word in words:
##        score = score + len(user_word)
##        print(f"correct your score is {score}")
##    else:
##        print("your answer is wrong")
##print("Thank you so much")


letters = [['h','o','l','i','d','a','y'],
           ['p','r','o','g','r','a','m','m','i','n','g'],
           ['b','o','o','t','c','a','m','p'],
           ['f','l','o','w','c','h','a','r','t'],
           ['w','o','r','d','s','c','a','p','e','s']]
words = [["hi","hay","day","had","lay","dal","lad","lid","hold","lady","hail"],
         ["go","an","in","no","on","map","mom","gap","gag","pig","man","ping",
          "pong","pram","prom","ramp"],
         ["am","at","to","cab","cap","cob","cop","map","mop","act","bat","camp",
          "comb","boom","pact","atom"],
         ["of","at","or","to","caw","cow","how","who","calf","claw","flaw","flow",
          "fowl","wolf","crow","half"],
         ["we","do","as","cap","caw","cop","cow","paw","cod","dew","pad","cape",
          "cope","crap","crew","crop"]];

lives = 5;
level = 0;
score = 0;

while level<5:
    print('Level',level+1) #('Level {}'.format(level+1))
    print('Create 3 words using the given letters')
    break

    for c in letters[level]:
        continue
        print('{}\t'.format(c),end='');
    print()
    
    
    
    
