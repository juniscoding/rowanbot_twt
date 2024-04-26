import os
import tweepy
import json
from random import randint

with open('quotes.json') as quotes:
    data = json.load(quotes)

bot = tweepy.Client(
    #Consumer Keys
    consumer_key= os.environ['CONSUMER_KEY'],
    consumer_secret= os.environ['CONSUMER_SECRET'],
    # Access Token and Secret
    access_token= os.environ['ACCESS_TOKEN'],
    access_token_secret= os.environ['ACCESS_TOKEN_SECRET'])

def post_quotes():
	book = random.choice(data.keys())
    book_quotes = data[book]
    random_index = randint(0, len(book_quotes)-1)
    quote = book_quotes[random_index]
    r = bot.create_tweet(text=quote)
    print(r)
    return None