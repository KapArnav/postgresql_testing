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

class DatabaseOperations:
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
            logger.info(f"Successfully connected to database {self.database}")
        except psycopg2.OperationalError as e:
            logger.error(f"Failed to connect to database: {e}")
            self.connection = None

    def insert_employee(self, name, position, salary, hire_date):
        if self.connection is None:
            logger.warning("No database connection. Cannot insert employee.")
            return
        
        try:
            with self.connection.cursor() as cursor:
                insert_query = """
                INSERT INTO employees (name, position, salary, hire_date)
                VALUES (%s, %s, %s, %s);
                """
                cursor.execute(insert_query, (name, position, salary, hire_date))
                self.connection.commit()
                logger.info(f"Employee {name} inserted successfully!")
        except Exception as e:
            logger.error(f"Failed to insert employee: {e}")

    def fetch_employees(self):
        if self.connection is None:
            logger.warning("No database connection. Cannot fetch employees.")
            return []
        
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM employees;")
                employees = cursor.fetchall()
                logger.info(f"Fetched {len(employees)} employees.")
                return employees
        except Exception as e:
            logger.error(f"Failed to fetch employees: {e}")
            return []
    
    def close_connection(self):
        if self.connection:
            self.connection.close()
            logger.info("Database connection closed.")
        else:
            logger.warning("No connection to close.")
