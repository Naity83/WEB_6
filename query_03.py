import logging
from psycopg2 import DatabaseError
from connect import create_connection

if __name__ == '__main__':
    sql_expression_03 = """
       SELECT g.group_name, ROUND(AVG(gr.grade), 2) AS average_grade
        FROM grades gr
        JOIN students s ON gr.student_id = s.id
        JOIN groups g ON s.group_id = g.id
        JOIN subjects subj ON gr.subject_id = subj.id
        WHERE subj.subject = 'Фізика'
        GROUP BY g.group_name;
        """
    try:
        with create_connection() as conn:
            if conn is not None:
                c = conn.cursor()
                try:
                    c.execute(sql_expression_03,)
                    print(c.fetchall())
                except DatabaseError as e:
                    logging.error(e)
                finally:
                    c.close()
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)