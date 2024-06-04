from datetime import datetime
from typing import Dict, Optional, Any, List

import pydantic


class Project(pydantic.BaseModel):
    """Project model."""
    id: str = pydantic.Field(alias='projectId')
    name: str = pydantic.Field(alias='projectName')
    description: Optional[str] = pydantic.Field(default=None, alias='projectDescription')

    scope: Optional[str] = pydantic.Field(default=None, alias='projectScope')
    permissions: Optional[Dict] = pydantic.Field(default=None, alias='projectPermissions')

    is_archived: bool = pydantic.Field(default=None, alias='projectIsArchived')
    archive_date: Optional[str] = pydantic.Field(default=None, alias='projectArchiveDate')

    create_date: Optional[str] = pydantic.Field(default=None, alias='projectCreateDate')
    update_date: Optional[str] = pydantic.Field(default=None, alias='projectUpdateDate')
    start_date: Optional[str] = pydantic.Field(default=None, alias='projectStartDate')
    end_date: Optional[str] = pydantic.Field(default=None, alias='projectEndDate')
    issue_settings: Optional[Dict] = pydantic.Field(default=None, alias='issueSettings')

    users: Optional[List[Dict]] = pydantic.Field(default=None, alias='projectUsers')

    application_connect: Optional[str] = pydantic.Field(default=None, alias='applicationConnect', repr=False)
    connection_id: Optional[str] = pydantic.Field(default=None, alias='projectConnectionId', repr=False)
    connection_name: Optional[str] = pydantic.Field(default=None, alias='connectionName', repr=False)
    last_incoming_pong: Optional[str] = pydantic.Field(default=None, alias='lastIncomingPong', repr=False)
    last_outgoing_ping: Optional[str] = pydantic.Field(default=None, alias='lastOutgoingPing', repr=False)
    connection: Optional[Any] = pydantic.Field(default=None, alias='hive', repr=False, exclude=True)

    model_config = pydantic.ConfigDict(
        populate_by_name=True
    )

    @pydantic.field_validator('create_date', 'update_date', 'start_date', 'end_date', mode='before')
    def validate_datetime(cls, value: str) -> str:
        """Validate datetime field."""
        try:
            dt: datetime = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError:
            raise ValueError('Invalid datetime.')
        return datetime.strftime(dt, '%d-%m-%Y %H:%M:%S')

    def __str__(self) -> str:
        """Return string representation of object."""
        return f'{self.__class__.__name__}({"".join(f"{key}={value}, " for key, value in self.model_dump().items())})'
