import pymysql
import pandas as pd
def creat_table(conn, cur):
    try:
        query = '''
        create table customers
        (name varchar(10),
        category smallint,
        region varchar(10))
        '''
        cur.execute(query)
        conn.commit()
        print('table 생성 완료')

    except Exception as e:
        print(e)
        
def main():
    conn = pymysql.connect(host = 'localhost', user='root',password='hanlim0691', db = 'sqlclass_db', charset='utf8')
    cur = conn.cursor()
    creat_table(conn,cur)
    
    
    cur.close()
    conn.close()
    print('데이터 베이스 연결 종료')

main()

conn =	pymysql.connect(host='localhost',	user='root', password='hanlim0691',
db='sqlclass_db', charset='utf8')
cur = conn.cursor()
sql ='''insert into     
customers(name, category, region)
values(%s, %s, %s)'''
cur.execute(sql, ('홍길동', 1, '서울'))
cur.execute(sql, ('이연수', 2, '서울'))
conn.commit()
print('INSERT 완료')
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


# executemany()
# 여러개의 tuple을 한번에 처리