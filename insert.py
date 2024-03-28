import logging
from functools import wraps
from random import randint
from faker import Faker
from psycopg2 import DatabaseError
from connect import create_connection

fake = Faker('uk_UA')  # Ініціалізуємо Faker з українською локаллю

def handle_database_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except DatabaseError as e:
            logging.error(e)
            conn.rollback()
    return wrapper

@handle_database_errors
def insert_groups(conn, sql_expression: str):
    c = conn.cursor()
    for group_name in ['Група 1', 'Група 2', 'Група 3']:
        c.execute(sql_expression, (group_name,))
    conn.commit()
    c.close()

@handle_database_errors
def insert_teachers(conn, sql_expression: str):
    c = conn.cursor()    
    for teacher_name in ['Іванов Іван', 'Петров Петро', 'Сидоров Сидор']:
        c.execute(sql_expression, (teacher_name,))
    conn.commit()
    c.close()

@handle_database_errors
def insert_subjects(conn, sql_expression: str):
    c = conn.cursor()
    subjects = [
        ('Математика', 1), ('Фізика', 2), ('Хімія', 3),
        ('Історія', 1), ('Література', 2), ('Географія', 3)
    ]
    for subject, teacher_id in subjects:
        c.execute(sql_expression, (subject, teacher_id))
    conn.commit()
    c.close()

@handle_database_errors
def insert_students(conn, sql_expression: str):
    c = conn.cursor()    
    for group_id in range(1, 4):
        for _ in range(15):
            c.execute(sql_expression, (fake.name(), group_id))
    conn.commit()
    c.close()

@handle_database_errors
def insert_grades(conn, sql_expression: str):
    c = conn.cursor()
    for student_id in range(1, 46):
        for subject_id in range(1, 7):
            for _ in range(3):
                grade = randint(0, 100)
                grade_date = fake.date_between(start_date='-1y', end_date='today')
                c.execute(sql_expression, (subject_id, student_id, grade, grade_date))
    conn.commit()
    c.close()

if __name__ == '__main__':
    
    sql_insert_groups = """
        INSERT INTO groups (group_name) VALUES (%s);
        """
    sql_insert_teachers = """
        INSERT INTO teachers (fullname) VALUES (%s);
        """
    sql_insert_subjects = """
        INSERT INTO subjects (subject, teacher_id) VALUES (%s, %s);
        """
    sql_insert_students = """
        INSERT INTO students (fullname, group_id) VALUES (%s, %s);
        """
    sql_insert_grades = """
        INSERT INTO grades (subject_id, student_id, grade, grade_date) VALUES (%s, %s, %s, %s);
        """
    try:
        with create_connection() as conn:
            if conn is not None:
                insert_groups(conn, sql_insert_groups)
                insert_teachers(conn, sql_insert_teachers)
                insert_subjects(conn, sql_insert_subjects)
                insert_students(conn, sql_insert_students)
                insert_grades(conn, sql_insert_grades)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)
