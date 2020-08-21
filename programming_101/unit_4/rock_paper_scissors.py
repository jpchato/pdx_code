import random

choice = input('Do you choose rock, paper, or scissors? ')
choice = choice.lower()
rps = ['rock', 'paper', 'scissors']
random_choice = random.choice(rps)

if choice == random_choice:
    print(f'{choice} is your choice and {random_choice} is the random choice')
    print('tie') 
elif choice =='rock' and random_choice=='paper':
    print(f'{choice} is your choice and {random_choice} is the random choice')
    print('lose')
elif choice == 'rock' and random_choice=='scissors':
    print(f'{choice} is your choice and {random_choice} is the random choice')
    print('win')
elif choice == 'paper' and random_choice=='rock':
    print(f'{choice} is your choice and {random_choice} is the random choice')
    print('lose')
elif choice == 'paper' and random_choice=='scissors':
    print(f'{choice} is your choice and {random_choice} is the random choice')
    print('lose')
elif choice == 'scissors' and random_choice=='rock':
    print(f'{choice} is your choice and {random_choice} is the random choice')
    print('lose')
elif choice == 'scissors' and random_choice=='paper':
    print(f'{choice} is your choice and {random_choice} is the random choice')
    print('win')

