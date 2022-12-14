"""
Title: twitter_api_module.py
Developer: Kevin Wu
Description: Webscraper module for Twitter URLs.
"""

import tweepy
from dotenv import dotenv_values

"""
Twitter Bearer Token From .env File

To generate a key:
https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens
"""
file = dotenv_values(".env")
bearer_token = file["BEARER_TOKEN"]

"""
Login to tweepy using a Twitter bearer token.

@param bearer_token is the user's bearer token
@return the tweepy client
"""
def login(bearer_token):
    client = tweepy.Client(bearer_token=bearer_token)
    return client

"""
Validate that the given link is for a Twitter tweet.
Looks for "twitter.com" and "status" in the specific positions in the link, then returns the ID of the tweet.
Ends the program if the URL is invalid.

@param url is the URL of the tweet
@return the tweet ID if valid or -1 if invalid
"""
def validate_link(url):
    url_split = url.split('/')
    if (len(url_split) == 6 and (url_split[-4] == "twitter.com" and url_split[-2] == "status")):
        tweet_id = url_split[-1]
        tweet_id = tweet_id.split('?')   # remove excess characters after tweet ID
        tweet_id = tweet_id[0]
        return tweet_id
    else:
        return -1

"""
Return the text from a tweet.

@param client is the tweepy client
@param tweet_id is the id of the tweet to get
@return the tweet
"""
def open_tweet_link(client, tweet_id):
    tweet = client.get_tweet(id=tweet_id)
    return tweet

"""
Return the text of a tweet given a url.

@param url is the url of the tweet
@return the text contained in the tweet, or empty string if bearer token is empty
"""
def return_text(url):
    if bearer_token == "":
        return ""
    client = login(bearer_token)
    tweet_id = validate_link(url)
    tweet = open_tweet_link(client, tweet_id)
    return tweet.data.text

"""
Main function. Takes a bearer token and url to extract text from a tweet.
Exit if bearer token is empty.
"""
def main():
    if bearer_token == "":
        exit(1)
    url = "https://twitter.com/NetflixAnime/status/1573896580507344896"
    client = login(bearer_token)
    tweet_id = validate_link(url)
    if tweet_id == -1:
        print("URL is not a link to a tweet.")
        exit(1)
    tweet = open_tweet_link(client, tweet_id)
    print(tweet.data.text)

"""
Main function guard.
"""
if __name__ == "__main__":
    main()