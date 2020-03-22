import postgre_connector
import  twitter_connector
import tweepy

api = twitter_connector.create_api()
cur = postgre_connector.connect()

followers = tweepy.Cursor(api.followers).items()
for item in followers:
    # print('name: ' + item.name + '\n' + 'user_name: ' + item.screen_name + '\n'+ 'followers: '+  str(item.followers_count))
    
