import logging
from psycopg2 import DatabaseError
from connect import create_connection

if __name__ == '__main__':
    sql_expression_11 = """
        SELECT ROUND(AVG(g.grade), 2) AS average_grade
        FROM grades g
        JOIN subjects sj ON g.subject_id = sj.id
        JOIN teachers t ON sj.teacher_id = t.id
        JOIN students s ON g.student_id = s.id
        WHERE t.fullname = 'Іванов Іван'
        AND s.fullname = 'Зорян Ященко';
        """
    try:
        with create_connection() as conn:
            if conn is not None:
                c = conn.cursor()
                try:
                    c.execute(sql_expression_11,)
                    print(c.fetchall())
                except DatabaseError as e:
                    logging.error(e)
                finally:
                    c.close()
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)