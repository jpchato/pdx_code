import string
import random 

def password_generator():
    char = string.ascii_letters + string.digits + string.punctuation
    print (random.choice(char))
    password = ''
    while len(password) < 10:
        password = password + random.choice(char)
    print(password)

if __name__ == "__main__":
    password_generator()