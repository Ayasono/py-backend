from fastapi import FastAPI
import psycopg2

app = FastAPI()

# database params
conn_params = {
    'dbname': 'shop',
    'user': 'postgres',
    'password': 'qQ7539518462',
    'host': 'localhost',
    'port': '5432'    
}

# connect
try:
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()

    # execute
    cursor.execute('SELECT version();')
    db_version = cursor.fetchone()
    print(f'PostgreSQL database version: {db_version}')

    # close
    cursor.close()
    conn.close()
except Exception as e:
    print(f'Error: {e}')
    
@app.get("/")
def read_root():
    return {"Hello": "World"}
