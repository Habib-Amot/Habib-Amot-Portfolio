import sqlite3

cursor = sqlite3.connect('db.sqlite3')
cursor.execute('DROP UsingModels_businessorders')
cursor.close