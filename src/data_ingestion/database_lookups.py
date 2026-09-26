"""Script for scanning database table for APIs and Schemas"""
import pgsql
from models.resource import ApiResource

def lookup_resources(
        database_url: str,
        database_user: str,
        database_password: str,
        database_db: str,
        database_api_resource_table: str
) -> list[ApiResource]:
    """Looks up APIs and Schemas"""
    db = pgsql.Connection(
        address=database_url,
        user=database_user,
        password=database_password,
        database=database_db,
    )
    api_resources = []
    with db.prepare(f"SELECT * FROM {database_api_resource_table};", ApiResource) as resources:
        for resource in resources:
            api_resources.append(resource)
    db.close()
    return api_resources
