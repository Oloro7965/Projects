import string
import random
print('welcome to the password generator'.center(40))
print('='*40)
number_passwords=int(input('Type the number of passwords you desire to have '))
password_length=int(input('Type how many characters you want your password to have '))
characters= string.ascii_letters + string.digits + string.punctuation
passwords=[]
for number in range(number_passwords):
    password=''
    for character in range(password_length):
        # print(random.choice(caracteres),end='')
        password+=random.choice(characters)
    passwords.append(password)
print('here are your passwords')
for element in passwords:
    print(element)