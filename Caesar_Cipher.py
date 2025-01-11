e=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
want="yes"
def encryption(shift,message):
     text=""
     for char in message:
        if char in e:
            text+=e[(e.index(char)+shift)%26]
        else:
            text+=char
     print(f"Here's the encrypted result:  {text}")
def decryption(shift,message):
                text=""
                for char in message:
                    if char in e:
                        n=e.index(char)-shift
                        if(n>0):
                            text+=e[n%26]
                        else:
                            n=n+26
                            text+=e[n%26]
                    else:
                        text+=char
                print(f"here's the decrypted result: {text}")
while(want=="yes"):
    print("Type 'encrypt' for encryption, type 'decrypt' for decryption: ")
    choose=input("")
    print("Type your message: ")
    message=input("")
    print("Type the shift number: ")
    shift=int(input(""))
    if(choose=='encrypt'):
         encryption(shift,message)
    elif(choose=='decrypt'):
         decryption(shift,message)
    print("if you want enter yes or else no")
    want=input("")


        







