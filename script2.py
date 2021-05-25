import psycopg2


def create_table():
    conn = psycopg2.connect(
        "dbname='database1' user='postgres' password='postgres2021' host='localhost' port='5432' ")
    cur = conn.cursor()
    # create execute method and create a table and describe table name as store
    cur.execute(
        "CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    # commit change
    conn.commit()
    # close connection
    conn.close()


def insert(item, quantity, price):
    # connect with database
    conn = psycopg2.connect(
        "dbname='database1' user='postgres' password='postgres2021' host='localhost' port='5432' ")
    # create cursor object
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    # commit change
    conn.commit()
    # close connection
    conn.close()


def view():
    conn = psycopg2.connect(
        "dbname='database1' user='postgres' password='postgres2021' host='localhost' port='5432' ")
    cur = conn.cursor()
    # select data from table
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect(
        "dbname='database1' user='postgres' password='postgres2021' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = psycopg2.connect(
        "dbname='database1' user='postgres' password='postgres2021' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",
                (quantity, price, item))
    conn.commit()
    conn.close()


create_table()
insert('meat', 20, 25)
delete('apple')
update(10, 10.5, 'meat')
print(view())
