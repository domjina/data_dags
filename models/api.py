"""Dataclass for API structure"""
from dataclasses import dataclass
from datetime import datetime

@dataclass
class API: # pylint: disable=too-many-instance-attributes
    """Dataclass for API structure"""
    api_id: int

    # Identity
    name: str
    description: str | None
    provider: str

    # Connection
    base_url: str
    version: str | None
    connection_id: str | None

    # API Capabilities
    paginated: bool
    supports_incremental: bool
    supports_bulk: bool

    # Rate limiting
    rate_limit_requests: int | None
    rate_limit_period_seconds: int | None
    locked: bool
    locked_until: datetime | None

    # Usage
    last_accessed: datetime | None
    last_downloaded: datetime | None

    # Operational state
    enabled: bool
    status: str
    last_success: datetime | None
    last_failure: datetime | None
    last_error: str | None

    # Audit
    created_at: datetime
    updated_at: datetime

    # Misc
    additional: dict | None
    override: dict | None
