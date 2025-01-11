import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
         'r','s','t','u','v','w','x','z','y','A','B','C','D','E','F','G','H','I',
         'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols=['!','@','#','$','%','^','&','*','(',')','/','|']
numbers=['1','2','3','4','5','6','7','8','9','0']
print("Welcome to the Password Generator!")
n_letters=int(input("How many letters would you like in your password? "))
n_symbols=int(input("How many symbols would you like in your password? "))
n_numbers=int(input("How many numbers would you like in your password? "))
password_list=[]
for i in range(n_letters):
    password_list+=random.choice(letters)
for i in range(n_symbols):
    password_list+=random.choice(symbols)
for i in range(n_numbers):
    password_list+=random.choice(letters)
print(password_list)
random.shuffle(password_list)
password=""
for char in password_list:
    password+=char
print(password)


