import tweepy
from django.conf import settings

def fetch_tweets(query, count=10):
    auth = tweepy.OAuth1UserHandler(
        settings.TWITTER_API_KEY,
        settings.TWITTER_API_SECRET,
        settings.TWITTER_ACCESS_TOKEN,
        settings.TWITTER_ACCESS_TOKEN_SECRET,
    )
    api = tweepy.API(auth)
    tweets = api.search_tweets(q=query, count=count, tweet_mode="extended")
    return [
        {
            "username": tweet.user.screen_name,
            "text": tweet.full_text,
            "created_at": tweet.created_at,
            "likes": tweet.favorite_count,
            "retweets": tweet.retweet_count,
        }
        for tweet in tweets
    ]
