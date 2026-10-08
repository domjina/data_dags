"""Common functions used by different DAGs"""

def fetch_table_records(postgres_conn_id, table) -> list[tuple]:
    """Return records from table in Postgres"""
    from airflow.providers.postgres.hooks.postgres import PostgresHook

    hook =  PostgresHook(postgres_conn_id)
    results = hook.get_records(f"SELECT * FROM {table};")
    return results
