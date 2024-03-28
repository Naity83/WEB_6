import logging
from psycopg2 import DatabaseError
from connect import create_connection

if __name__ == '__main__':
    sql_expression_02 = """
        SELECT s.id, s.fullname, ROUND(AVG(g.grade), 2) AS avg_grade
        FROM students s
        JOIN grades g ON s.id = g.student_id
        JOIN subjects sj ON g.subject_id = sj.id
        WHERE sj.subject = 'Математика'
        GROUP BY s.id, s.fullname
        ORDER BY avg_grade DESC
        LIMIT 1;



        """
    try:
        with create_connection() as conn:
            if conn is not None:
                c = conn.cursor()
                try:
                    c.execute(sql_expression_02,)
                    print(c.fetchall())
                except DatabaseError as e:
                    logging.error(e)
                finally:
                    c.close()
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)