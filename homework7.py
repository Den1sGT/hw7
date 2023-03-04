import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = False
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table(conn,sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)


def create_student(conn,student):
    sql = '''INSERT INTO student(fullname,mark,hobby)
    VALUES(?,?,?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql,student)
        conn.commit()
    except Error as e:
        print(e)


def read_student(conn):
    try:
        sql = '''SELECT * FROM student'''
        cursor = conn.cursor()
        cursor.execute()
        conn.commit()
    except Error as e:
        print(e)

def delete_student(conn):
    sql = "DELETE FROM student WHERE id =?"
    try:
        cursor = conn.cursor()
        cursor.execute()
        conn.commit()
    except Error as e:
        print(e)




