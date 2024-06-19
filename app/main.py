from fastapi import FastAPI
import psycopg2
import json
import os

app = FastAPI()

# Read database connection parameters from config file
config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'database_config.json')
with open(config_path, 'r') as config_file:
    conn_params = json.load(config_file)

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
