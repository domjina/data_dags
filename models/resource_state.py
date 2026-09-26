"""Dataclass for API resource state"""
from dataclasses import dataclass
from datetime import datetime

@dataclass
class ApiResourceState: # pylint: disable=too-many-instance-attributes
    """Dataclass for API resource state"""
    resource_id: str

    cursor: str | None

    last_run: datetime | None
    last_success: datetime | None
    next_run: datetime | None

    rows_loaded: int
    bytes_loaded: int

    status: str
    last_error: str | None

    updated_at: datetime
