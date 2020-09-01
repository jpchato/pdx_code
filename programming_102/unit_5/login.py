user_profile = {
    'username' : 'jpchato',
    'password' : 'p@$$w0rd'
}

def login(username, password):

  
    # print(username)
    # print(user_profile.get('username'))

    # print(password)
    # print(user_profile.get('password'))


    if user_profile.get('username') == username and password == user_profile.get('password'):
        print('Login successful')
        return True
    
    elif user_profile.get('username') != username or password != user_profile.get('password'):
        print('Failed login')
        return False

        
def repl_login():
    username = input('What is your username? ')
    password = input('What is your password? ')

    login_attempts = 0

    while login_attempts <= 3:
        login_attempts += 1
        if user_profile.get('username') == username and password == user_profile.get('password'):
            print('Login successful')
            return True
        elif user_profile.get('username') != username or password != user_profile.get('password'):
            print('Failed login')
            if login_attempts == 3:
                print(f'You have tried {login_attempts}. Login attempts have been exceeded')
                return False
            username = input('What is your username? ')
            password = input('What is your password? ')
        # else:
        #     username = input('What is your username? ')
        #     password = input('What is your password? ')
    
        

if __name__ == "__main__":
    # login('jpchato', 'p@$$w0rd')
    # login('sdaflhk', 'sdalfkjdasf')
    repl_login()