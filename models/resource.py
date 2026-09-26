"""Dataclass for API resource structure"""
from dataclasses import dataclass
from datetime import datetime

@dataclass
class ApiResource: # pylint: disable=too-many-instance-attributes
    """Dataclass for API resource structure"""
    resource_id: str
    api_id: str

    name: str
    endpoint: str
    method: str

    parameters: dict | None

    api_key_ref: str

    pagination_type: str | None
    pagination_config: dict | None

    incremental_strategy: str | None
    incremental_field: str | None
    initial_value: str | None

    schedule: str | None

    destination: str | None
    destination_table: str | None

    enabled: bool

    created_at: datetime
    updated_at: datetime

    additional: dict | None
    override: dict | None
