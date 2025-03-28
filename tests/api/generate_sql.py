import requests

database_struct = """
{'territories': {'check_constraints': [],
    'columns': [{'autoincrement': False,
                'comment': None,
                'default': None,
                'name': 'territory_id',
                'nullable': False,
                'type': VARCHAR(length=20)},
                {'autoincrement': False,
                'comment': None,
                'default': None,
                'name': 'territory_description',
                'nullable': False,
                'type': VARCHAR(length=60)},
                {'autoincrement': False,
                'comment': None,
                'default': None,
                'name': 'region_id',
                'nullable': False,
                'type': SMALLINT()}],
    'comments': {'text': None},
    'foreign_keys': [{'comment': None,
                    'constrained_columns': ['region_id'],
                    'name': 'fk_territories_region',
                    'options': {},
                    'referred_columns': ['region_id'],
                    'referred_schema': None,
                    'referred_table': 'region'}],
    'indexes': [],
    'primary_keys': {'comment': None,
                    'constrained_columns': ['territory_id'],
                    'name': 'pk_territories'},
    'unique_constraints': []}}
"""

response = requests.post(
    url=f"http://localhost:9876/generate/sql/",
    json={
        "query": "Liste todos os clientes",
        "database_struct": database_struct
    }
)

print(response.json())