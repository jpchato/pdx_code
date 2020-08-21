# 2.1

def guess():
    answer = 'z'
    
    letter = input('Guess a letter: ')

    if answer == letter:
        print('correct answer')

    else: 
        print('the correct answer was z')

# 2.2 & 2.3

def guess_again():
    word = input('type a word: ')

    letter = input('type a letter: ')
    
    if letter in word:
        letter_count = word.count(letter)
        print(f'{letter.upper()} is in {word} {letter_count} times')
    else:
        print(f'{letter.upper()} is not in {word}')

#2.4


if __name__ == "__main__":
    guess()
    guess_again()