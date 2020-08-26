'''
Two words are anagrams of each other if the letters of one can be rearranged to fit the other. e.g. dormitory and dirtyroom.

Write a program that lets the user enter two strings, and tells them if they are anagrams of each other.

Convert the strings into lists (list)
Sort the letters of each word (sort)
Check if the two are equal
'''

# reference https://stackoverflow.com/a/4978792

def anagram_checker(word_1, word_2):
    print(f'Checking if {word_1} and {word_2} are an anagram')
    list_1 = list(word_1)
    list_2 = list(word_2)
    list_1.sort()
    list_2.sort()

    if list_1 == list_2:
        print('It\'s an anagram')
    else:
        print('It\'s not an anagram')


if __name__ == "__main__":
    anagram_checker('dormitory', 'dirtyroom')
    anagram_checker('howdy', 'doody')