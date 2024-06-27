import sqlite3
 
try:
    sqliteConnection = sqlite3.connect('learnbuddy_42.db')
    cursor = sqliteConnection.cursor()

    query = 'select * FROM phonic_level;'
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

    cursor.close()
except sqlite3.Error as error:
    print('Error occurred - ', error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
    
    