import logging
from psycopg2 import DatabaseError
from connect import create_connection

if __name__ == '__main__':
    sql_expression_06 = """
        SELECT s.fullname
        FROM students s
        WHERE s.group_id = 2;

        """
    try:
        with create_connection() as conn:
            if conn is not None:
                c = conn.cursor()
                try:
                    c.execute(sql_expression_06,)
                    print(c.fetchall())
                except DatabaseError as e:
                    logging.error(e)
                finally:
                    c.close()
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)