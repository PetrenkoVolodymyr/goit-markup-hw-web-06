from faker import Faker
from random import randint
from sqlite3 import Error
from connect import create_connection, database

fake = Faker()

def create_data(conn):
    cur = conn.cursor()
    try:
        for i in range(1, 4):
            cur.execute("INSERT INTO groups (id, groups) VALUES (?, ?)", (i , fake.word()))
        conn.commit()
        for i in range(1, 6):
            cur.execute("INSERT INTO teachers (id, teacher) VALUES (?, ?)", (i , fake.name()))
        conn.commit()
        for i in range(1, 40):
            cur.execute("INSERT INTO students (id, student, gruop_id) VALUES (?, ?, ?)", (i , fake.name(), randint(1,3)))
        conn.commit()
        for i in range(1,7):
            cur.execute("INSERT INTO subjects (id, topics, teacher_id) VALUES (?, ?, ?)", (i , fake.word(), randint(1,5)))
        conn.commit()
        n=1
        for st in range(1,40):
            for su in range(1,7):
                for i in range(1,15):
                    cur.execute("INSERT INTO marks (id, mark, marker_at, student_id, subject_id) VALUES (?, ?, ?, ?, ?)", (n , randint(1,5), fake.date_this_decade(), st, su))
                    n+=1
        conn.commit()

    except Error as e:
        print(e)
    finally:
        cur.close()

    return cur.lastrowid


if __name__ == '__main__':  
    with create_connection(database) as conn:
        
        create_data(conn)

