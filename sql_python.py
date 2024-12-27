import psycopg2

host = "localhost"
database = "postgres"
user = "postgres"
password = "***"

try:
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )   
    cur = conn.cursor ()
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        position VARCHAR (100),
        salary NUMERIC (10, 2),
        hire_date DATE
    );
    """
    cur.execute(create_table_query)
    conn.commit()
    print("table is created successfully!")    
    
    cur.close ()
    conn.close()
    
except Exception as e:
    print(f"An error occurred: {e}")