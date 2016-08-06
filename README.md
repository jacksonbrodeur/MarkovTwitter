# MarkovTwitter

This is a program that reads through a user's public tweets and using Markov chains creates a new tweet by following patterns found in that user's tweets.

## Usage

First you need to run get_tweets.py to retrieve the tweets and save them to a file. This is done by running `python3 get_tweets.py user_name` where `user_name` is the twitter handle of the desired user.

After this is done, run generate_tweet.py to create a tweet based on the tweet data of a user. Note: you must run get_tweets.py before generate_tweet.py for a specific user. To run this script do `python3 generate_tweet.py user_name` where `user_name` is the twitter handle of the desired user.

#### TODO
Create a Django app that provides a nice web-based front end to this functionality