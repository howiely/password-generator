import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!-?,@$'

pw_amount = input("Enter the amount of passwords you'd like to generate: ")
pw_amount = int(pw_amount)

pw_length = input('Enter the desired password length: ')
pw_length = int(pw_length)

for p in range(pw_amount):
    password = ''
    for c in range(pw_length):
        password += random.choice(chars)
    print(password)