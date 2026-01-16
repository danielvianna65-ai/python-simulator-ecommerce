import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="admin",
        password="NovaSenhaForte123!",
        database="ecommerce",
        autocommit=False  # IMPORTANTE (transações)
    )
