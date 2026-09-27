"""Return records from respective tables"""
from airflow.providers.postgres.hooks.postgres import PostgresHook

def fetch_table_records(postgres_conn_id, table) -> list[tuple]:
    """Return records from table"""
    hook =  PostgresHook(postgres_conn_id)
    results = hook.get_records(f"SELECT * FROM {table};")
    return results
