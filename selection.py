import sqlite3


def execute_query(file) -> list:
    with sqlite3.connect('test.db') as con:
        cur = con.cursor()
        with open(file, 'r') as f:
            sql = f.read()
        cur.execute(sql)
        return cur.fetchall()
    
task = input('inpet task number -> ')
file = 'query_'+task+'.sql'
print(execute_query(file))
