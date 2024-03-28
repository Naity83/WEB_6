#Встановими зєднання з базою даних
import psycopg2  # Імпортуємо бібліотеку psycopg2 для роботи з PostgreSQL
from contextlib import contextmanager  # Імпортуємо декоратор contextmanager з модуля contextlib

@contextmanager
def create_connection():
    try:
        """ create a database connection to database """
        # Встановлюємо з'єднання з базою даних PostgreSQL
        conn = psycopg2.connect(host="localhost", database="homework", user="postgres", password="150209")
        yield conn  # Повертаємо з'єднання для використання в блоку with
        conn.close()  # Закриваємо з'єднання після завершення роботи з ним
    except psycopg2.OperationalError as err:
        raise RuntimeError(f"Failed to create database connection {err}")  # Обробляємо помилку під час створення з'єднання з базою даних
