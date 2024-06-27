import sqlite3
 
try:
    sqliteConnection = sqlite3.connect('learnbuddy_42.db')
    cursor = sqliteConnection.cursor()

    for x in range(1, 137):
        _sql = 'insert into phonic_level (id) values (?);'
        cursor.execute(_sql,(x,))
    sqliteConnection.commit()

    cursor.close()
except sqlite3.Error as error:
    print('Error occurred - ', error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
