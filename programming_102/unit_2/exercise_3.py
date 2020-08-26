'''
2.1
Define a function called generate_password().

The function will not require parameters and will return a ten-character password.

The character pool from which the ten characters are selected should contain uppercase letters, lowercase letters, digits (0-9) and some kind of special characters.
'''

import string
import random 

def generate_password():
    char = string.ascii_letters + string.digits + string.punctuation
    password = ''
    while len(password) < 10:
        password = password + random.choice(char)
    print(password)

'''
2.2
Add a parameter to your function which will allow the user to pass the number of characters they want in their password. Require a minimum of 8.

If the user enters less than 8 for the character count, display a message and tell them they need at least 8 characters.
'''

def generate_specific_password(password_length):
    char = string.ascii_letters + string.digits + string.punctuation
    password = ''
    while password_length < 8:
            password_length = int(input('Your password needs at least 8 characters '))
    if password_length >= 8:
        while len(password) < password_length:
            password = password + random.choice(char)
    print('Your password is ' + str(password) + ' and it is ' + str(len(password)) + ' characters long')
    


'''
2.3
Allow the user to choose how many letters, numbers, and punctuation characters they want in their password. Mix everything up using list(), random.shuffle(), and ''.join().

You may want to define another function, get_random_chars(), to choose from each set of characters to avoid writing more code than is necessary.

get_random_chars() will require two parameters, the characters from which to select the characters and a quantity of characters to select from the characters.

get_random_chars() will return a list containing the quantity of each set of characters that the user provides.
'''

def get_random_chars():
    pass

def specific_password():
    pass


if __name__ == "__main__":
    generate_password()
    generate_specific_password(7)