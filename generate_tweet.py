import pickle
import random
import sys

def triples(words):
    if len(words) < 3:
        return

    for i in range(len(words) - 2):
        yield (words[i], words[i + 1], words[i + 2])

if __name__ == '__main__':
    tweets = []
    cache = {}
    if len(sys.argv) < 2:
        print("Usage: python3 generate_tweet.py screen_name")
        sys.exit(2)

    file_name = "tweets_{}.in".format(sys.argv[1])
    try:
        tweet_file = open(file_name, "rb")
        tweets = pickle.load(tweet_file)
        tweet_file.close()
    except:
        print("There was an error opening '{}'".format(file_name))
        sys.exit(2)

    for tweet in tweets:
        text = tweet['text']
        if not text.endswith((".", "!", "?")):
            text += "."
        words = text.split(" ")
        #words = [w.lower() for w in words]
        words = [w for w in words if  "http" not in w and ".com" not in w]
        words = [w for w in words if not w.isspace()]
        words = [w for w in words if w]
        words = [w.replace(" ", "") for w in words]
        words = [w.replace("&amp;", "&") for w in words]
        for(w1, w2, w3) in triples(words):
            key = (w1, w2)
            if key in cache:
                cache[key].append(w3)
            else:
                cache[key] = [w3]

    success = False
    count = 0
    while not success:
        w1 = "a"
        w2 = ""
        while w1[0].islower() and w1[0].isalpha() or w1.isspace():
            w1, w2 = random.choice(list(cache.keys()))
        new_tweet = ""
        try:
            count += 1
            while len(new_tweet) < 140:
                new_tweet += w1 + " "
                w1, w2 = w2, random.choice(cache[(w1,w2)])
        except:
            continue
        success = True
        new_tweet += w2
        new_tweet = new_tweet[:min(140, len(new_tweet))]
        possible_end = []
        possible_end.append(new_tweet.rfind("?"))
        possible_end.append(new_tweet.rfind("."))
        possible_end.append(new_tweet.rfind("!"))
        j = max(possible_end)
        if j == -1:
            j = len(new_tweet) - 1
        new_tweet = new_tweet[:j+1]
        print(new_tweet)
        print("Length: {}".format(len(new_tweet)))