'''
Define a function called clean_text() that takes in some text as a parameter.

remove all new line characters \n from the text
remove all punctuation from the text
convert the entire text to lowercase
use the .split() method to split the text at every space, creating a list of individual words
Finally, return the list of lower case words with no punctuation.
'''

def clean_text(text):
    stripped_text = text.strip('\n')
    punc_stripped_text = stripped_text.strip('''!()-[]\{\};:'"\, <>./?@#$%^&*_~''')
    almost = punc_stripped_text.lower()
    done = almost.split(' ')
    print (done)

if __name__ == "__main__":
    clean_text('asdfkj 12321! !@#$!$@ \n asdfklj!@#3333')


