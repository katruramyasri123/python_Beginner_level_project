import random
print("WELCOME THE HANGMAN GAME")
list=['apple']
word=random.choice(list)
print(word)
blanks=[];
for i in range(len(word)):
    blanks+='_'
print(blanks)
print(" Actually THE LIFETIME IS 6.... if you guess wrong the chances are decreased")
lifetime=6
while(lifetime!=0 and '_' in blanks):
    user_letter=input("guess a letter: ")
    for i in range(len(word)):
        if(user_letter not in word):
            lifetime-=1
            print(blanks)
            if(lifetime==1):
                print("alert! you have only chance so play carefully..")
            break;
      
        elif(word[i]==user_letter and blanks[i]=='_'):
            blanks[i]=user_letter
            print(blanks)
            break

        else:
            if(i==len(word)-1):
                lifetime-=1
                print(blanks)
                if(lifetime==1):
                    print("alert! you have only one chance")
            else:
                pass;
   
if(lifetime!=0):
    print("user win")
    print(f"the word is {word}")
else:
    print("computer win")