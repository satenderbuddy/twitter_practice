import psycopg2

def connect():
    try:
        conn = psycopg2.connect("dbname =twitter user=postgres password=1234")
        cur = conn.cursor()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return cur,conn

def close_conn(cur, conn):
    cur.close()
    conn.close()

def create_my_follower(is_new, name, u_name, follower_count, cur, conn):
    sql = ''' INSERT INTO public.my_followers(name, user_name, is_new, followers_count) 
              values(%s,%s,%s,%s) RETURNING id;'''
    id = None
    try:
        cur.execute(sql,(name, u_name, is_new, follower_count))
        id = cur.fetchone()[0]
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return id

def view_my_followers():
    cur,conn = connect()
    sql = ''' Select id, user_name from public.my_followers where id is not null'''
    cur.execute(sql)
    followers = cur.fetchall()
    for follower in followers:
        print('id: ', follower[0],'username: ', follower[1])
    close_conn(cur,conn)

def create_my_following(name, u_name, follower_count, cur, conn):
    sql = ''' INSERT INTO public.my_following(name, username, followers_count) 
              values(%s,%s,%s) RETURNING id;'''
    id = None
    try:
        cur.execute(sql,(name, u_name, follower_count))
        id = cur.fetchone()[0]
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return id