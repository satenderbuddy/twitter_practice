import postgre_connector
import  twitter_connector
import tweepy
import time

menu = ''' ___________________________________________
|___Welcome to Twitter Mod App______________|
|       1: My Profile                       |
|       2: My Following list                |
|       3: My Followers list                |
|       4: Refresh my followers list        |
|       5: Refresh my following list        |
|       6: Send request to 15 new people    |
|       7: Unfollow who didn't follow back  |
|       8: Retrieve excel of followers      |
|       9: Retrieve excel of followers      |
|___________________________________________|'''

def create_followers_db():
    api = twitter_connector.create_api()
    cur,conn = postgre_connector.connect()
    followers = tweepy.Cursor(api.followers).items()
    for item in followers:
        id = postgre_connector.create_my_follower(False, item.name, item.screen_name, item.followers_count, cur, conn)
        if id == None:
            print("record not created")

    postgre_connector.close_conn(cur,conn)

def view_my_profile(uname):
    api = twitter_connector.create_api()
    me = api.get_user(uname)
    print("Name:\t", me.name)
    print("User Name:\t", me.screen_name)
    print("Followers:\t", me.followers_count)
    print("Following:\t", me.friends_count)

def view_my_followers(me):
    cur,conn = postgre_connector.connect()
    sql ="SELECT user_name, name from public.my_followers where id is not null"
    cur.execute(sql)
    followers = cur.fetchall()
    print("My Followers: ")
    for follower in followers:
        print("Name: " + follower[1] + "\tUser Name: " + follower[0])
    postgre_connector.close_conn(cur,conn)



def view_my_following(me):
    cur,conn = postgre_connector.connect()
    sql ="SELECT username, name from public.my_following where id is not null"
    cur.execute(sql)
    followers = cur.fetchall()
    print("My followings: ")
    for follower in followers:
        print("Name: " + follower[1] + "\tUser Name: " + follower[0])
    postgre_connector.close_conn(cur,conn)

def refresh_my_followers(me):
    print("Not Implemented yet")

def refresh_my_following(me):
    print("Not Implemented yet")

def send_req_to_new_people(me):
    print("Not Implemented yet")

def unfollow_not_followback(me):
    print("Not Implemented yet")

def print_excel_followers(me):
    print("Not Implemented yet")

def print_excel_following(me):
    print("Not Implemented yet")

def choose(i):
        switcher={
            0:view_my_profile,
            1:view_my_followers,
            2:view_my_following,
            3:refresh_my_followers,
            5:refresh_my_following,
            6:send_req_to_new_people,
            7:unfollow_not_followback,
            8:print_excel_followers,
            9:print_excel_following
            }
        return switcher.get(i,"Invalid option")