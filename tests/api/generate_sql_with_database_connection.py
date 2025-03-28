import requests

database_connection_config_id = 1

response = requests.post(
    url=f"http://localhost:9876/generate/sql/{database_connection_config_id}/",
    json={
        "query": "Find customer with most orders and number of orders made",
        "only_sql": False
    }
)

print(response.status_code, response.json())
