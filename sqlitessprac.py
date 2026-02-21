import sqlite3
conn = sqlite3.connect("naya.db")
cursor = conn.cursor()#interact with db thru sql

#cursor.execute('''
  #             CREATE TABLE IF NOT EXISTS users(
   #            id integer primary key,
    #            age integer,
    #          email text unique)
    #  '''  )
#conn.commit()
#cursor.execute('insert into users(username,age,email)values("ali",22,"al@gmail.com")')
#conn.commit()
#users=[
#    ('bob',25,'bob@2xamp.com'),
 #   ('charlie',33,'char@gmail.com')
#]
#cursor.executemany("insert into users(username,age,email)values(?,?,?)",users)
#conn.commit()
cursor.execute("select*from users")
rows= cursor.fetchall()
for row in rows:
    print (row)
cursor.execute("select*from users where age>30")
filtered_rows=cursor.fetchall()
for row in filtered_rows:
      print(row)
cursor.execute("update users set age = 100,email='changareuy@gmail.com'where username = 'ali'")
conn.commit()
cursor.execute("delete from users where username = 'charlie'")#so yesley chai table nai delete gardinxa
conn.commit()
conn.close()