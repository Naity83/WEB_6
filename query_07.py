import logging
from psycopg2 import DatabaseError
from connect import create_connection

if __name__ == '__main__':
    sql_expression_07 = """
        SELECT s.fullname, g.grade
        FROM grades g
        JOIN students s ON g.student_id = s.id
        JOIN subjects subj ON g.subject_id = subj.id
        JOIN groups grp ON s.group_id = grp.id
        WHERE grp.group_name = 'Група 2' AND subj.subject = 'Фізика';
        """
    try:
        with create_connection() as conn:
            if conn is not None:
                c = conn.cursor()
                try:
                    c.execute(sql_expression_07,)
                    print(c.fetchall())
                except DatabaseError as e:
                    logging.error(e)
                finally:
                    c.close()
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)