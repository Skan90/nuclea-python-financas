import psycopg2

def return_db_connection_params():
    connection_params = {
        "user": "postgres",
        "password": "postgres",
        "port": "5432",
        "host": "localhost",
        "database": "nuclea"
    }