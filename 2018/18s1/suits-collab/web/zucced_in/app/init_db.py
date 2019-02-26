#!/usr/bin/python3

import sqlite3, hashlib

database = 'test.db'

admin_un = "admin"
admin_name = "Mr Admin FLAG{Safebook_might_be_a_misnomer}"
admin_em = "zac@unswsecurity.com"
admin_pw_unsafe = "There once was a hero named"
admin_pw = hashlib.md5(admin_pw_unsafe.encode("utf")).hexdigest()

testuser_un = "user"
testuser_name = "Test User"
testuser_em = "zacheryellis@gmail.com"
testuser_pw_unsafe = "password"
testuser_pw = hashlib.md5(testuser_pw_unsafe.encode("utf")).hexdigest()

def repopulate_users(c):    
	# Create table
    try:
        c.execute('''DROP TABLE users''')
    except:
        pass
    c.execute('''CREATE TABLE users
    (username TEXT PRIMARY KEY, name TEXT, email TEXT, password TEXT)''')
    
    c.execute('''INSERT INTO users(username, name, email, password) VALUES(?,?,?,?)''',
                (admin_un, admin_name, admin_em, admin_pw))
    c.execute('''INSERT INTO users(username, name, email, password) VALUES(?,?,?,?)''',
                (testuser_un, testuser_name, testuser_em, testuser_pw))

def main():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    repopulate_users(cursor)
    connection.commit()
    connection.close()
    print("Setup complete")

if __name__ == "__main__":
    main()