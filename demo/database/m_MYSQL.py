# coding=utf-8

import mysql.connector as connector

try:
    conn = connector.connect(user='root', password='root', database='test')
    cursor = conn.cursor()
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'February'])
    conn.commit()

    cursor.execute('select * from user')
    values = cursor.fetchall()
    print(values)

finally:
    cursor.close()
    conn.close()