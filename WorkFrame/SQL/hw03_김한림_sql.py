import pymysql
import pandas as pd
# 구동에 필요한 함수 구현

def main():
    conn = pymysql.connect(host = 'localhost', user='root',password='hanlim0691', db = 'sqlclass_db', charset='utf8')
    cur = conn.cursor()
    
    sql ="""
        create table user_table
            (userID CHAR(8) not null,
            userName VARCHAR(10) not null,
            birthYear INT not null,
            addr CHAR(2) not null,
            mobile1 CHAR(3),
            mobile2 CHAR(8),
            height SMALLINT,
            mDate DATE,
            constraint pk_userID primary key (userID)
           )
           """
    create_table(conn, cur,sql)
   
    sql ="""
        insert into user_table
        (userID, userName, birthYear, addr, mobile1, mobile2, height, mDate)     
        values
        (%s, %s, %s, %s, %s, %s, %s, %s)
        """
    data = (
            ('KHD', '강호동', 1970, '경북', '011','22222222', 182, '2007-07-07'),
            ('KJD', '김제동', 1974, '경남', '', '', 173, '2013-03-03'),
            ('KKJ', '김국진', 1965, '서울', '019', '33333333', 171, '2009-09-09'),
            ('KYM', '김용만', 1967, '서울', '010', '44444444', 177, '2015-05-05'),
            ('LHJ', '이휘재', 1972, '경기', '011', '88888888', 180, '2006-04-04'),
            ('LKK', '이경규', 1960, '경남', '018', '99999999', 170, '2004-12-12'),
            ('NHS', '남희석', 1971, '충남', '016', '66666666', 180, '2017-04-04'),
            ('PSH', '박수홍', 1970, '서울', '010', '00000000', 183, '2012-05-05'),
            ('SDY', '신동엽', 1971, '경기', '', '', 176, '2008-10-10'),
            ('YJS', '유재석', 1972, '서울', '010', '11111111', 178, '2008-08-08')
            )
    insert_into(conn, cur, sql, data)
    
    sql ="""
            create table buy_table
			(num INT auto_increment not null,
            userID CHAR(8) not null,
            prodName CHAR(6) not null,
            groupName CHAR(4),
            price INT not null,
            amount SMALLINT not null,
            constraint pk_num primary key (num),
            constraint fk_fav_num_userID foreign key (userID)
            references user_table(userID)
            )
            """
    create_table(conn, cur, sql)
    sql ="""
        insert into buy_table
        (num, userID, prodName, groupName, price, amount)        
        values
        (%s, %s, %s, %s, %s, %s)
        """
    data = (
            (1, 'KHD', '운동화', '', 30, 2),
            (2, 'KHD', '노트북', '전자', 1000, 1),
            (3, 'KYM', '모니터', '전자', 200, 1),
            (4, 'PSH', '모니터', '전자', 200, 5),
            (5, 'KHD', '청바지', '의류', 50, 3),
            (6, 'PSH', '메모리', '전자', 80, 10),
            (7, 'KJD', '책', '서적', 15, 5),
            (8, 'LHJ', '책', '서적', 15, 2),
            (9, 'LHJ', '청바지', '의류', 50, 1),
            (10, 'PSH', '운동화', '', 30, 2),
            (11, 'LHJ', '책', '서적', 15, 1),
            (12, 'PSH', '운동화', '', 30, 2)
            )
    insert_into(conn, cur, sql, data)
    
    print('1번 문제 테이블 생성 완료')
    print('2-1번')
    query = """
        select ut.userName, bt.prodName, ut.addr, concat(ut.mobile1, ut.mobile2) as 연락처
            from user_table as ut
            inner join buy_table as bt
            on ut.userID = bt.userID
    """
    read_table(cur,query)
    print('2-2번')
    
    query = """
    select info.userID, info.userName,   info.prodName, info.addr, info.연락처
        from 
            (select ut.userID, ut.userName, bt.prodName, ut.addr, concat(ut.mobile1, ut.mobile2) as 연락처
            from user_table as ut
            inner join buy_table as bt
            on ut.userID = bt.userID) as info
        where userID = 'KYM'
        """
    read_table(cur,query)
        
    print('2-3번')
    query = """
        select ut.userID, ut.userName, bt.prodName, ut.addr, concat(ut.mobile1, ut.mobile2) as 연락처
        from user_table as ut
            inner join buy_table as bt
            on ut.userID = bt.userID
        order by ut.userID ASC
        """
    read_table(cur,query)

    print('2-4번')
    query = """
        select distinct ut.userID, ut.userName,  ut.addr
        from user_table as ut
            inner join buy_table as bt
            on ut.userID = bt.userID
        order by ut.userID ASC
        """
    read_table(cur,query)
    
    print('2-5번')
    query = """
    select ut.userID, ut.userName, ut.addr, concat(ut.mobile1, ut.mobile2) as 연락처
            from user_table as ut
            inner join buy_table as bt
            on ut.userID = bt.userID
            where ut.addr = '경북' or ut.addr = '경남'
        """
    read_table(cur,query)
    
    cur.close()
    conn.close()

def create_table(conn, cur, sql):
    conn = pymysql.connect(host = 'localhost', user='root',password='hanlim0691', db = 'sqlclass_db', charset='utf8')
    cur = conn.cursor()
    try: 
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        
def insert_into(conn, cur, sql, data):
    conn = pymysql.connect(host = 'localhost', user='root',password='hanlim0691', db = 'sqlclass_db', charset='utf8')
    cur = conn.cursor()
    try: 
        cur.executemany(sql, data)
        conn.commit()
    except Exception as e:
        print(e)
        
def read_table(cur,query):
    conn = pymysql.connect(host = 'localhost', user='root',password='hanlim0691', db = 'sqlclass_db', charset='utf8')
    cur = conn.cursor()
    try:
        cur.execute(query)
        rows = cur.fetchall()#데이터를 가져옴
        result_df = pd.DataFrame(rows)
        print('-'*result_df.shape[1])
        for i in result_df.columns:
            print(i, end = '    ')
        print()
        for j in range(0,result_df.shape[0]):
            print(result_df.iloc[j])
    except Exception as e:
        print(e)


main()
