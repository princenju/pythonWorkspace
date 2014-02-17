import mysql.connector
conn=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='test')
c=conn.cursor()
c.execute('show tables')
print c.fetchall()
c.close()
conn.close()