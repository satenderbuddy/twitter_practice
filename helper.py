import postgre_connector
import  twitter_connector
import tweepy
import time

menu = ''' ___________________________________________
|___Welcome to Twitter Mod App______________|
|       1: My Profile                       |
|       2: My Followers list                |
|       3: My Followings list               |
|       4: Refresh my followers list        |
|       5: Refresh my following list        |
|       6: Send request to 15 new people    |
|       7: Unfollow who didn't follow back  |
|       8: Retrieve excel of followers      |
|       9: Retrieve excel of followers      |
|___________________________________________|'''


def view_my_profile(uname):
    api = twitter_connector.create_api()
    me = api.get_user(uname)
    info = "Name:\t" + me.name
    info += "     User Name:\t" + me.screen_name
    info += "\nFollowers:\t" + str(me.followers_count)
    info += "     Following:\t" + str(me.friends_count)
    return info

def view_my_followers():
    cur,conn = postgre_connector.connect()
    sql ="SELECT user_name, name from public.my_followers where id is not null"
    cur.execute(sql)
    followers = cur.fetchall()
    print("My Followers: ", len(followers))
    for follower in followers:
        print("Name: " + follower[1] + "\tUser Name: " + follower[0])
    postgre_connector.close_conn(cur,conn)

def view_my_following():
    cur,conn = postgre_connector.connect()
    sql ="SELECT username, name from public.my_following where id is not null"
    cur.execute(sql)
    followers = cur.fetchall()
    print("My followings: ")
    for follower in followers:
        print("Name: " + follower[1] + "\tUser Name: " + follower[0])
    postgre_connector.close_conn(cur,conn)

def refresh_my_followers():
    api = twitter_connector.create_api()
    cur,conn = postgre_connector.connect()
    followers = tweepy.Cursor(api.followers).items()
    followers_ids = []
    for item in followers:
        followers_ids.append(item.screen_name)
        if not postgre_connector.is_in_db(item.screen_name):
            try:
                id = postgre_connector.create_my_follower(item.name, item.screen_name, item.followers_count, cur, conn)
            except Exception as e:
                print(e.error)
                continue
        else:
            continue
    postgre_connector.del_left_users(followers_ids)
    postgre_connector.close_conn(cur,conn)

def refresh_my_following():
    refresh_my_followers(me)
    api = twitter_connector.create_api()
    cur,conn = postgre_connector.connect()
    followings = tweepy.Cursor(api.friends).items()
    for item in followings:
        try:
            id = postgre_connector.create_my_following(item.name, item.screen_name, item.followers_count, postgre_connector.check_follow_back(item.screen_name), cur, conn)
        except Exception as e:
            print("error: ",e)
            print("exception type", type(e))
            continue

    postgre_connector.close_conn(cur,conn)

def send_req_to_new_people():
    print("Not Implemented yet")

def unfollow_not_followback():
    print("Not Implemented yet")

def print_excel_followers():
    print("Not Implemented yet")

def print_excel_following(me):
    print("Not Implemented yet")

def choose(i):
        switcher={
            0:view_my_profile,
            1:view_my_followers,
            2:view_my_following,
            3:refresh_my_followers,
            4:refresh_my_following,
            5:send_req_to_new_people,
            6:unfollow_not_followback,
            7:print_excel_followers,
            8:print_excel_following
            }
        return switcher.get(i,"Invalid option")