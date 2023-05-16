import sqlite3 as sql


username = input(f"Username:")
password = input(f"Password:")
con = sql.connect("users.db")
cur = con.cursor()
statement = f"SELECT username from users WHERE username='{username}' AND nacl_pwhash = '{password}';"
cur.execute(statement)
if not cur.fetchone():  # An empty result evaluates to False.
    print("Login failed")
else:
    print("Welcome")