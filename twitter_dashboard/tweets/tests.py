import tweepy

# Twitter API Keys
API_KEY = "Bv7nQpC07yIGWdiBa0t8uXx6F"
API_SECRET = "O4zShDTZNzUcB0l0Tu53DwZlpB3GVAY1w7AfiphdZrw3O6XUyJ"
ACCESS_TOKEN = "1248595637932679174-Uq5J9dHOhtHT16AU0GshDMfYOWgLfE"
ACCESS_SECRET = "vCnvxu62eIaFFHBVG6P6CkxDLhSIXa6SjznDpFWzgroDA"



def test_twitter_api():
    try:
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        client = tweepy.API(auth, wait_on_rate_limit=True)
        
        # Test the connection by fetching your timeline
        tweets = client.home_timeline(count=1)
        for tweet in tweets:
            print(f"Tweet by {tweet.user.name}: {tweet.text}")
        print("Twitter API is working correctly!")
    except Exception as e:
        print(f"Error: {e}")

test_twitter_api()
