import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:

# 作业
# -*- coding: utf-8 -*-

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

conn = sqlite3.connect('../files/student.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS student')
cursor.execute('CREATE TABLE student (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20), score INT)')
cursor.execute(r"INSERT INTO student VALUES ('A-001', 'Adam', 95)")
cursor.execute(r"INSERT INTO student VALUES ('A-002', 'Bart', 62)")
cursor.execute(r"INSERT INTO student VALUES ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low, high):
    conn, cursor = None, None
    try:
        conn = sqlite3.connect('../files/student.db')
        cursor = conn.cursor()
        cursor.execute('SELECT name FROM student WHERE score BETWEEN ? AND ? ORDER BY score', (low, high))
        return [n[0] for n in cursor.fetchall()]
    finally:
        cursor.close()
        conn.commit()
        conn.close()
# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')