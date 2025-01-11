import random
import math
system=random.randint(1,50)
guesses=math.log(50,2)
maximum_guesses=round(guesses)
i=1;
while i<maximum_guesses:
    if(i==maximum_guesses-1):
        print("hey!This is your last trial")    
    user=int(input("enter a number"))
    if(system==user):
        print("hurry! you guessed right..")
        print(f"no of guesses{i}")
        break;
    else:
        if(i==maximum_guesses-1):
            print(f"sorry! And the answer is {system}")
        else:
            if(user<system):
                 print(" please try again you guessed too low")
            else:
                 print(" please try again you guessed too hign")
             
        i+=1
        



