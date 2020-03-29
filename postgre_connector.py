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

def create_my_follower(name, u_name, follower_count, cur, conn):
    sql = ''' INSERT INTO public.my_followers(name, user_name, followers_count) 
              values(%s,%s,%s) RETURNING id;'''
    id = None
    try:
        cur.execute(sql,(name, u_name, follower_count))
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

def create_my_following(name, u_name, follower_count, follow_back, cur, conn):
    sql = ''' INSERT INTO public.my_following(name, username, followers_count, follow_back) 
              values(%s,%s,%s,%s) RETURNING id;'''
    id = None
    try:
        cur.execute(sql,(name, u_name, follower_count, follow_back))
        id = cur.fetchone()[0]
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return id

def check_follow_back(screen_name):
    cur,conn = connect()
    sql = '''SELECT name, user_name FROM public.my_followers where user_name = %s '''
    cur.execute(sql,(screen_name,))
    if cur.fetchone() is not None :
        close_conn(cur,conn)
        return True
    else:
        close_conn(cur,conn)
        return False

def del_left_users(followers):
    sql = """SELECT user_name FROM public.my_followers WHERE id is not null"""
    cur,cunn = connect()
    cur.execute(sql)
    followers_db = cur.fetchall()
    for_del = []
    for follower_db in followers_db:
        if follower_db[0] not in followers:
            delete_from_db(follower_db[0],cur,cunn)

def delete_from_db(follower,cur, cunn):
    sql = """DELETE FROM public.my_followers WHERE user_name = %s;"""
    cur.execute(sql,(follower,))
    if cur.rowcount:
        print("deleted record:",cur.rowcount)
        cunn.commit()
    else:
        print("deleted nothing")

def is_in_db(u_name):
    cur,cunn = connect()
    sql = """SELECT user_name FROM public.my_followers WHERE user_name = %s"""
    cur.execute(sql,(u_name,))
    if cur.fetchone() is not None:
        return True
    else:
        return False