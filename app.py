'''Importing files for connection to db and password hasing.'''
import sqlite3
from nacl import pwhash
from nacl.exceptions import InvalidkeyError
import FixExchangeQuery

OPS_LIMIT = pwhash.OPSLIMIT_MODERATE
MEM_LIMIT = pwhash.MEMLIMIT_MODERATE

conn = sqlite3.connect('users.db')

# cursor = conn.cursor().execute('''
# CREATE TABLE IF NOT EXISTS users (
#     username VARCHAR(16) PRIMARY KEY,
#     nacl_pwhash VARCHAR(100)
# )
# ''')

# def create_account(username, password):
#     '''This function is used to create account in users table.'''
#     cursor = conn.cursor()
#     cursor.execute('SELECT count(*) FROM users WHERE username=?', (username,))
#     result = cursor.fetchone()
#     if result[0] > 0:
#         raise Exception('Username already taken')

#     hashed = pwhash.str(bytes(password, 'UTF-8'),
#         opslimit=OPS_LIMIT,
#         memlimit=MEM_LIMIT,
#     )
#     cursor.execute('INSERT INTO users (username, nacl_pwhash) VALUES (?, ?)', (username, hashed))
#     conn.commit()


def login():
    '''This is the main as after login the FixExchange gets executed!'''
    username=input("Username:")
    password=input("Password:")
    cursor = conn.cursor()
    cursor.execute('SELECT nacl_pwhash FROM users WHERE username=?', (username,))
    result = cursor.fetchone()
    if result is None:
        raise ValueError('Invalid username or password')

    if result is None:
        # User doesn't exist. Make sure the login is still slow.
        pwhash.str(b'',
            opslimit=OPS_LIMIT,
            memlimit=MEM_LIMIT,
        )
        raise ValueError('Invalid username or password')

    try:
        pwhash.verify(result[0], bytes(password, 'UTF-8'))
    except Exception as error:
        raise InvalidkeyError('Invalid Username or Password') from error
    if result is not None:
        print("Welcome!")
        FixExchangeQuery.exchange()

# Make a couple accounts for demonstration
# create_account('admin','password')


# try:
#     # Attempt to log in
#     login('jim', 'password')
#     print('Login succeeded')
# except Exception as e:
#     print(f'Login error: {e}')

if __name__ == "__main__":
    login()
