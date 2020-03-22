import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("bt65ie1Ne3cXcAV5DX40UVmjC")
    consumer_secret = os.getenv("IoFQfPPsWvLYoIaKf1ZbGrtHjLJdfBSc5r39z4eNnoDVd1TqX5")
    access_token = os.getenv("856153663814983681-4wmsSL3muUJCMfNvirGSWozEx15L7GM")
    access_token_secret = os.getenv("kMQIAX308hCgHzVHxIxwYLA5ApKG5FVqeZMtbXeb6OTOP")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api

