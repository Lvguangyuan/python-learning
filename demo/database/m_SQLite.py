# -*- coding: utf-8 -*-

import sqlite3

'''
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
'''

try:
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    start = input('score start:')
    end = input('score end:')
    sql = 'select name from student where score < ? and score > ?'
    cursor.execute(sql, (end, start))
    values = cursor.fetchall()
    print(values)

finally:
    cursor.close()
    conn.close()

