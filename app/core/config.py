import json
import os

config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'database_config.json')
with open(config_path, 'r') as config_file:
    conn_params = json.load(config_file)

DATABASE_URL = f"postgresql://{conn_params['user']}:{conn_params['password']}@{conn_params['host']}:{conn_params['port']}/{conn_params['dbname']}"
