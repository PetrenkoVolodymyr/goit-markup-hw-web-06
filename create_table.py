from sqlite3 import Error

from connect import create_connection, database


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


if __name__ == '__main__':
    sql_create_teachers_table = """
    CREATE TABLE IF NOT EXISTS teachers (
    id INT PRIMARY KEY,
    teacher VARCHAR(30)
    );
    """

    sql_create_groups_table = """
    CREATE TABLE IF NOT EXISTS groups (
    id INT PRIMARY KEY,
    groups VARCHAR(30)
    );
    """

    sql_create_students_table = """
    CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    student VARCHAR(30),
    gruop_id INT,
    FOREIGN KEY (gruop_id) REFERENCES groups (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
    );
    """

    sql_create_subjects_table = """
    CREATE TABLE IF NOT EXISTS subjects (
    id INT PRIMARY KEY,
    topics VARCHAR(30),
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
    );
    """

    sql_create_marks_table = """
    CREATE TABLE IF NOT EXISTS marks (
    id INT PRIMARY KEY,
    mark INT,
    marker_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    student_id INT,
    subject_id INT,
    FOREIGN KEY (student_id) REFERENCES students (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
    );
    """



    with create_connection(database) as conn:
        if conn is not None:

            create_table(conn, sql_create_groups_table)
            create_table(conn, sql_create_teachers_table)
            create_table(conn, sql_create_students_table)
            create_table(conn, sql_create_subjects_table)
            create_table(conn, sql_create_marks_table)

        else:
            print("Error! cannot create the database connection.")
