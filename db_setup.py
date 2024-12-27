import logging
import psycopg2

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log")
    ]
)

logger = logging.getLogger(__name__)

class DBSetup:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            logger.info(f"Connected to database {self.database}")
        except psycopg2.OperationalError as e:
            logger.error(f"Error connecting to database: {e}")
            self.connection = None

    def create_tables(self):
        if self.connection is None:
            logger.warning("No connection to create tables.")
            return
        
        try:
            with self.connection.cursor() as cursor:
                create_table_query = """
                CREATE TABLE IF NOT EXISTS employees (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    position VARCHAR(100),
                    salary NUMERIC(10, 2),
                    hire_date DATE
                );
                """
                cursor.execute(create_table_query)
                self.connection.commit()
                logger.info("Table created successfully.")
        except Exception as e:
            logger.error(f"Error creating table: {e}")
    
    def close_connection(self):
        if self.connection:
            self.connection.close()
            logger.info("Database connection closed.")
        else:
            logger.warning("No connection to close.")
