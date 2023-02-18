import pymysql
import pandas as pd
conn =	pymysql.connect(host='localhost',	user='root', password='hanlim0691',
db='sqlclass_db', charset='utf8')

cur = conn.cursor()
sql = """
    update customers
    set region = '서울특별시'
    where region = '서울'
"""
cur.execute(sql)
print('update 완료')

sql ='''
    delete from customers
    where name = %s
'''
cur.execute(sql, '홍길동')
print('홍길동')

conn.commit()
cur.close()
conn.close()


conn =	pymysql.connect(host='localhost',	user='root', password='hanlim0691',
db='sqlclass_db', charset='utf8')
cur = conn.cursor()
sql ='''select * from customers'''
cur.execute(sql)
rows = cur.fetchall()
print('불러오기 완료')
customer = pd.DataFrame(rows)
print(customer)
cur.close()
conn.close()