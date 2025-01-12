def Continue(result):
        choice=input("enter y to continue with {result} or n to start with new calcalution or x to exit: ")
        if choice=='n':
            pass
        elif choice=='x':
            global end_of_operation
            end_of_operation=True
        else:
            Result(result)
def addition(first,second):
    add=first+second
    print(f"{first} + {second}={add}")
    Continue(add)
def subtraction(first,second):
    sub=first-second
    print(f"{first} - {second}={sub}")
    Continue(sub)
def multiplication(first,second):
    mul=first*second
    print(f"{first} * {second}={mul}")
    Continue(mul)
def division(first,second):
    div=first/second
    print(f"{first} / {second}={div}")
    Continue(div)
def Result(first):
    print("+\n-\n*\n/")
    operator=input("Pick an operation: ")
    second=int(input("enter next number: "))
    if operator=='+':
       addition(first,second)
    elif operator=='-':
        subtraction(first,second)
    elif operator=='*':
       multiplication(first,second)
    else:
       division(first,second)

end_of_operation=False
while not end_of_operation:
    first=int(input("enter first number: "))
    Result(first)

    
