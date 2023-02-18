import pymysql
import pandas as pd

conn = pymysql.connect(host = 'localhost', user='root',password='hanlim0691', db = 'sakila', charset='utf8')
cur = conn.cursor()
cur.execute('select * from language')
rows = cur.fetchall()#데이터를 가져옴
print(rows)
language_df = pd.DataFrame(rows)
print(language_df)
cur.close()
conn.close()#연결 종료


