import logging  # Імпортуємо модуль logging для роботи з логуванням
from psycopg2 import DatabaseError  # Імпортуємо клас DatabaseError з бібліотеки psycopg2

from connect import create_connection  # Імпортуємо функцію create_connection з модуля connect

def create_table(conn, sql_expression: str):
    c = conn.cursor()  # Створюємо курсор для виконання SQL-запитів
    try:
        c.execute(sql_expression)  # Виконуємо SQL-вираз для створення таблиці
        conn.commit()  # Зберігаємо зміни в базі даних
    except DatabaseError as e:  # Обробляємо виняток DatabaseError
        logging.error(e)  # Логуємо помилку
        conn.rollback()  # Скасовуємо зміни, якщо сталася помилка
    finally:
        c.close()  # Закриваємо курсор

if __name__ == '__main__':
    sql_create_groups_table = """
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    group_name VARCHAR(150) NOT NULL
);
"""

sql_create_students_table = """
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    group_id INTEGER NOT NULL REFERENCES groups(id),
    fullname VARCHAR(150) NOT NULL
);
"""

sql_create_teachers_table = """
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(150) NOT NULL
);
"""

sql_create_subjects_table = """
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    teacher_id INTEGER NOT NULL REFERENCES teachers(id),
    subject VARCHAR(150) NOT NULL
);
"""

sql_create_grades_table = """
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    subject_id INTEGER NOT NULL REFERENCES subjects(id),
    student_id INTEGER NOT NULL REFERENCES students(id),
    grade INTEGER CHECK (grade >= 0 AND grade <= 100) NOT NULL,
    grade_date DATE NOT NULL
);
"""

# Виконання кожного SQL-запиту окремо
try:
    with create_connection() as conn:
        if conn is not None:
            for query in [sql_create_groups_table, sql_create_students_table, sql_create_teachers_table,
                          sql_create_subjects_table, sql_create_grades_table]:
                conn.cursor().execute(query)
            conn.commit()
        else:
            print("Error! cannot create the database connection.")
except RuntimeError as err:
    logging.error(err)
    

