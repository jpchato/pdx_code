'''
You've got a very important message to get out to all your followers on Twitter. Unfortunately, Twitter only allows 280 characters per Tweet. Your message is over 1,000 characters long and you're wondering how many Tweets it will take to get your whole message out.

3.1
Calculate the number of Tweets required, rounding up to the nearest integer.

3.2
Ask the user for the number of characters in their message

if the length of the message is less than the max_length allowed for a Tweet, output a message telling the user they only need one Tweet

Otherwise, calculate the number of Tweets required, rounding up to the nearest integer and output a message telling the user the number of Tweets they will need.

3.3
Display different messages to the user depending on how many Tweets their message requires.
'''

# 3.1

tweet_length = 1000
tweet_max = 280
def tweets_required(tweet_length, tweet_max):
    tweets = tweet_length/tweet_max
    print(round(tweets))
    return round(tweets)

# 3.2 & 3.3
def users_characters():
    response = input('How many characters in your message: ')
    if int(response) < int(tweet_max):
        print('You only need to type one tweet')
        return 
    else: 
        tweets_ = int(response)/int(tweet_max)
        print(f'You need {round(tweets_)} tweets')
        if tweets_ > 3:
            print('consider shortening the message')
        


if __name__ == "__main__":
    tweets_required(tweet_length, tweet_max)
    users_characters()