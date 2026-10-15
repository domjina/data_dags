"""Create DAGs for each API resource"""
from airflow.sdk import dag, task
import datetime
import logging

postgres_conn_id = "local_postgres"
s3_conn_id = "garage-s3"

@dag(
    dag_id="download_data_dag",
    description="""
    This DAG retrieves all APIs from postgreSQL db,
    fetches all associated API resources, and downloads
    the latest data specified by the API resource.
    """,
    schedule="@daily",
    start_date=datetime.datetime(2026, 10, 16, 0, 0, 0),
    catchup=False
)
def dag_generator():
    @task
    def fetch_api_resources() -> list[dict]:
        from src.common import fetch_table_records
        apis = fetch_table_records(postgres_conn_id, "api")
        api_resources = fetch_table_records(postgres_conn_id, "api_resource")
        apis_by_id = {api["api_id"]: api for api in apis}
        return [
            {**apis_by_id[resource["api_id"]], **resource}
            for resource in api_resources
            if resource["api_id"] in apis_by_id
        ]

    @task
    def download_upload_latest_data(row: dict):
        import json
        from airflow.providers.amazon.aws.hooks.s3 import S3Hook
        from src.bureau_of_labour_stats.tools import fetch_data_bls_api, naming_convention_bls
        url = row["base_url"]
        endpoint = row["endpoint"]
        todays_year = datetime.datetime.now().year
        response = fetch_data_bls_api(
            url=url,
            series_id=[endpoint],
            start_year=str(int(todays_year)-10),
            end_year=str(todays_year)
        )
        file = json.dumps(response["series"][0]["data"]).encode("UTF-8")
        s3_hook = S3Hook(aws_conn_id=s3_conn_id)
        file_name = naming_convention_bls(row["name"], row["endpoint"])
        if not s3_hook.check_for_key(key=file_name):
            s3_hook.load_bytes(
                bytes_data=file,
                key=file_name,
                replace=False
            )
        else:
            logging.error(f"File {file_name} already in bucket; skipping upload")

    api_resources = fetch_api_resources()
    download_upload_latest_data.expand(
        row=api_resources
    )

download_data_dag = dag_generator()
