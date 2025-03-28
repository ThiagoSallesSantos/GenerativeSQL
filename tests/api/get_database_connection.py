import requests

database_connection_config_id = 1

response = requests.get(
    url=f"http://localhost:9876/database/{database_connection_config_id}/",
)

print(response.json())