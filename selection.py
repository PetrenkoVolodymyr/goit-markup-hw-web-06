from sqlite3 import Error

from connect import create_connection, database


def select_projects(conn):
    rows = None
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM marks;")
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return rows

if __name__ == '__main__':
    with create_connection(database) as conn:
        projects = select_projects(conn)
        print(projects)
