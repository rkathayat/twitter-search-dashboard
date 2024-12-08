import tweepy
from django.conf import settings

def fetch_tweets(query, count=10):
    client = tweepy.Client(
        bearer_token=settings.TWITTER_BEARER_TOKEN,
        consumer_key=settings.TWITTER_API_KEY,
        consumer_secret=settings.TWITTER_API_SECRET,
        access_token=settings.TWITTER_ACCESS_TOKEN,
        access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET,
    )
    
    response = client.search_recent_tweets(query=query, max_results=count, tweet_fields=['created_at', 'public_metrics'])
    
    if response.errors:
        print(f"Error: {response.errors}")
        return []
    
    tweets = response.data
    return [
        {
            "username": tweet.author_id,  # Note: Twitter API v2 does not return username directly
            "text": tweet.text,
            "created_at": tweet.created_at,
            "retweet_count": tweet.public_metrics['retweet_count'],
            "favorite_count": tweet.public_metrics['like_count'],
        }
        for tweet in tweets
    ]