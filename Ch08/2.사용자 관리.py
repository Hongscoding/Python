"""
날짜 : 2023/01/12
이름 : 홍민준
내용 : 파이썬 사용자 관리 실습하기
"""

import pymysql

conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       password='1234',
                       db='java1db',
                       charset='utf8')

while True:
    print('0:종료, 1:등록, 2:조회, 3:검색, 4:삭제')
    answer = 0
    try:
        answer = int(input('선택 : '))
    except Exception as e:
        print('다시 입력하세요.', e)
        continue

    if answer == 0:
        pass
    elif answer == 1:
        data = list(input('아이디, 비번, 이름, 휴대폰, 나이 순으로 입력 : ').split())
        cur = conn.cursor()
        sql = "insert into `user2` values ('%s', '%s', '%s', '%s', '%s')" 
        cur.execute(sql %(data[0], data[1], data[2], data[3], data[4]))
        conn.commit()

        print('등록완료')

    
    

    elif answer == 2:
        cur = conn.cursor()
        sql = "select * from `user2`" 
        cur.execute(sql)
        conn.commit()
        
        print('|아이디|비번|이름|휴대폰|나이|')

        for row in cur.fetchall():
            print('-------------------')
            print('|%s|%s|%s|%s|%s|' %(row[0],row[1],row[2],row[3],row[4]))

        print('조회 완료')


    elif answer == 3:
        name = input('이름 검색 : ')


        cur = conn.cursor()
        cur.execute("select * from `user2` where `name`='{}'".format(name) ) 
        conn.commit()
        
        print('|아이디|비번|이름|휴대폰|나이|')

        for row in cur.fetchall():
            print('-------------------')
            print('|%s|%s|%s|%s|%s|' %(row[0],row[1],row[2],row[3],row[4]))


        print('검색 완료')


    elif answer == 4:
        name = input('삭제할 이름 : ')
        cur = conn.cursor()
        cur.execute("delete from `user2` where `name`='{}'".format(name))
        conn.commit()

        print('삭제 완료')



    else:
        print('0 ~ 4 중에 입력')



#데이터 베이스 종료
conn.close()
print('종료')