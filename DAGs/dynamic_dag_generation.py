"""Create DAGs for each API resource"""
from airflow.sdk import dag, task

from src.data_ingestion.database_lookups import fetch_table_records

apis = fetch_table_records("", "")

resources = fetch_table_records("", "")
headers = resources[0]
resources = resources[1:]

resource_api = headers.index("api_id")

api_resources = {}
for resource in resources:
    if resource[resource_api] not in api_resources:
        api_resources[resource[resource_api]] = [resource]
    else:
        api_resources[resource[resource_api]].append(resource)

# FRED_id: {GDP_row, employment_row, ...}

for k, v in api_resources.items():
    @dag()
    def dynamic_resource_gen():
        @task
        def get_data():
            print("Hi")
    dynamic_resource_gen()
