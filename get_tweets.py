from twitter import *
import pickle
import sys
import configparser

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 get_tweets.py screen_name")
        sys.exit(2)


    config = configparser.ConfigParser()
    config.read("twitter_creds.ini")
    config = config['DEFAULT']
    t = Twitter(retry = True, auth=OAuth(config['token'], config['token_secret'], config['api_key'], config['api_secret']))

    all_tweets = []
    screen_name = sys.argv[1]
    tweets = t.statuses.user_timeline(screen_name = screen_name, include_rts = False)
    all_tweets.extend(tweets)
    oldest = all_tweets[-1]['id'] - 1

    while len(tweets) > 0:
        tweets = t.statuses.user_timeline(screen_name = screen_name, include_rts = False, max_id = oldest)
        all_tweets.extend(tweets)
        oldest = all_tweets[-1]['id'] - 1
        print("...{} tweets downloaded so far".format(len(all_tweets)))

    cache_file = open("tweets_{}.in".format(screen_name), "wb")
    pickle.dump(all_tweets, cache_file)
    cache_file.close()