import sqlite3


def create_table():
    # connect with database
    conn = sqlite3.connect("lite.db")
    # create cursor object
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
    conn = sqlite3.connect("lite.db")
    # create cursor object
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    # commit change
    conn.commit()
    # close connection
    conn.close()


insert('apple', 1, 2)


def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    # select data from table
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",
                (quantity, price, item))
    conn.commit()
    conn.close()


update(100, 20, 'juice')
print(view())
