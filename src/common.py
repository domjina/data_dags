"""Common functions used by different DAGs"""
def fetch_table_records(postgres_conn_id, table) -> list[dict]:
    """Return records from table in Postgres"""
    from airflow.providers.postgres.hooks.postgres import PostgresHook
    allowed_tables = {"api", "api_resource", "resource_state"}
    if table not in allowed_tables:
        raise ValueError(f"Unsupported table: {table}")
    
    hook =  PostgresHook(postgres_conn_id)

    with hook.get_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM \"{table}\";")
            columns = [desc[0] for desc in cursor.description]
            results = cursor.fetchall()
    return [
        dict(zip(columns, row))
        for row in results
    ]