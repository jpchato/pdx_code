import random

questions = ['What is your favorite color?', 'What is your favorite number?', 'What is your favorite planet?']

print('Welcome to the amazing Magic 8 Ball!')
question = input(random.choice(questions))
print(f'{question} is a perfectly valid choice!')