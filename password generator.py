import random
import string


def password_generate(pass_len):

    charvalues = string.ascii_letters + string.digits + string.punctuation


    password = ''

    for i in range(pass_len):
        password += random.choice(charvalues)

    print("Generated Password:", password)

#input from the user
pass_len = int(input("Enter the password length: "))

#functiion call
password_generate(pass_len)

