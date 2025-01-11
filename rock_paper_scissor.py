import random
user=int(input("enter the number"))
com=random.randint(0,2)
print(com)
if com==user:
    print("draw")
elif com==2 and user==0:
    print("user wins")
elif user==2 and com==0:
    print("computer wins")
elif com>user:
    print("computer wins")
elif user>com:
    print("user wins")
else:
    print("user invalid enter")