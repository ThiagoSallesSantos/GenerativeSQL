import requests

response = requests.post(
    url="http://localhost:9876/database/",
    json={
        "host": "localhost",
        "port": 2345,
        "database": "northwind_postgres",
        "username": "northwind_postgres", 
        "password": "northwind_postgres",
        "dbms": "postgresql"
    }
)

print(response.json())