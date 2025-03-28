import requests

database_connection_config_id = 2

response = requests.delete(
    url=f"http://localhost:9876/database/{database_connection_config_id}/",
)

print(response.json())
