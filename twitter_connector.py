import tweepy
from Configure import TwitterConfig


def create_api():
    auth = tweepy.OAuthHandler(TwitterConfig.consumer_key, TwitterConfig.consumer_secret)
    auth.set_access_token(TwitterConfig.access_token, TwitterConfig.access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    return api

