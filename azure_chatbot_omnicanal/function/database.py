import psycopg2 # type: ignore
import os
import logging

class DatabaseConnection:
    def __init__(self):
        self.connection = None

    def connect(self):
        if not self.connection:
            try:
                self.connection = psycopg2.connect(
                    host=os.environ["DB_HOST"],
                    database=os.environ["DB_NAME"],
                    user=os.environ["DB_USER"],
                    password=os.environ["DB_PASSWORD"],
                    port=os.environ.get("DB_PORT", 5432)
                    )
                logging.info('Conexión correcta con la base de datos')
            except Exception as e:
                logging.error('Error al realizar la conexion')
                raise Exception(f"Error al realizar la conexion")
        return self.connection
    
    def close(self):
        if self.connection:
            logging.info('Se finalizo la conexión')
            self.connection.close()
            self.connection = None