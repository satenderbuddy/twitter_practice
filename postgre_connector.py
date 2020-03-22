import psycopg2

def connect():
    try:
        conn = psycopg2.connect("dbname =twitter user=postgres password=1234")
        cur = conn.cursor()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return cur

def close_conn(cur, conn):
    cur.close()
    conn.close()

