from string import punctuation

def most_frequent(word_dict):
    '''
    This function takes in a dictionary and sorts the words by their value, then returns a dictionary with the ten most frequently occuring words
    '''
    pass


def main():
    '''
    read a text file
    count how many times each word in the text file occurs
    '''

    # open(file_name, read_write_mode) # open a file
    # the 'with' keyword makes opening an closing files easier

    with open('unit_5/alice.txt', 'r') as text_file:
        # file is open within this code block and is automatically closed when the code block ends

        dirty_text = text_file.read()

    # file is closed at this indentation
    # clean up the text
    # replace new line characters with spaces

    clean_text = dirty_text.replace('\n', ' ')

    # remove punctuation

    for punct in punctuation:
        clean_text = clean_text.replace(punct, '')

    # lowercase everythign
    clean_text = clean_text.lower()

    # split the text into individual words at the spaces

    word_list = clean_text.split(' ')

    # create a dictionary to store the words and their counts
    # the word is going to be the key and the count is going to be the value
    # word:count

    word_counts ={

    }

    # loop over the list and count all the words
    for word in word_list:
        # if the current word is not in word counts, add it as a key with a value of 1

        if word not in word_counts:
            word_counts[word] = 1

        # if the current word is already word_counts, add 1 to its value
        else:
            word_counts[word] += 1


        





    # print(word_list)
    print(word_counts)

if __name__ == "__main__":
    main()