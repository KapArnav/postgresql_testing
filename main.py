import logging
from db_setup import DBSetup
from db_operations import DatabaseOperations

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log")
    ]
)

logger = logging.getLogger(__name__)

host = "localhost"
database = "postgres"
user = "123"
password = "123"

db_setup = DBSetup(host, database, user, password)
db_setup.connect()
db_setup.create_tables()

db_ops = DatabaseOperations(host, database, user, password)
db_ops.connect()

try:
    db_ops.insert_employee("Alice", "Developer", 75000, "2024-01-15")
    db_ops.insert_employee("Bob", "Manager", 90000, "2024-02-20")
    
    employees = db_ops.fetch_employees()
    logger.info("Employees in the database:")
    for emp in employees:
        logger.info(emp)

except Exception as e:
    logger.error(f"An error occurred: {e}")

finally:
    db_setup.close_connection()
    db_ops.close_connection()
