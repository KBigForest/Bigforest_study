import pymysql
def insert_into(conn,cur):
# conn = pymysql.connect(host = 'localhost', user = 'root', password = 'hanlim0691', db = 'sqlclass_db', charset = 'utf8')
    try: 
        cur = conn.cursor()
        sql = '''
            insert into customers
            (name, category, region)
            values (%s, %s, %s)
        '''
        data = (
            ('홍진우',1,'서울'),
            ('강지수',2,'부산'),
            ('김청진',1,'대구')   
        )
        cur.executemany(sql, data)
        conn.commit()
        print('executemany() 완료')
    except Exception as e:
        print(e)
def main():
    conn = pymysql.connect(host = 'localhost', user = 'root', password = 'hanlim0691', db = 'sqlclass_db', charset = 'utf8')
    cur = conn.cursor()
    
    insert_into(conn,cur)
    cur.close()
    conn.close()
    