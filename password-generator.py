# password-generator.py

import random
# import random module from python

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!-?#@$_'
# characters used to generate passwords

pw_amount = input("Enter the amount of passwords you'd like to generate: ")
# input the amount of passwords to be generated
pw_amount = int(pw_amount)
# turns pw_amount from String -> Int

pw_length = input('Enter the desired password length: ')
# input the length of the generated password(s)
pw_length = int(pw_length)
# turns pw_length from String -> Int

for p in range(pw_amount):
    password = ''
    for c in range(pw_length):
        password += random.choice(chars)
    print(password)

# exit program after generation is complete
input("Password generation complete. Copy your passwords, then press ENTER/RETURN to exit the program.")