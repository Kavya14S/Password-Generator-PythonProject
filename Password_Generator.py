# PASSWORD GENERATOR
# WITH OUR OWN CHOICE OF NUMBER OF LETTERS,SYMBOLS AND NUMBERS

import random
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ['!','#','$','%','&','*','+','@','~','^']
password = []
print("Welcome to the Password Generator !")
a = int(input("How many letters would you like in your password?"))
for i in range(a):
    s = random.choice(alphabet)
    password.append(s)
b = int(input("How many symbols would you like in your password?"))
for i in range(b):
    s = random.choice(symbols)
    password.append(s)
c = int(input("How many numbers would you like in your password?"))
for i in range(c):
    s = random.choice(numbers)
    password.append(s)

random.shuffle(password)
final_password = ""
for i in password:
    final_password = final_password + str(i)
print(final_password)