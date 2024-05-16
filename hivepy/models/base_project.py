from datetime import datetime
from typing import Dict, Optional, Any

import pydantic

from hivepy.models.group import Group
from hivepy.models.unknown_hive_object import UnknownHiveObject


class BaseProject(UnknownHiveObject):
    id: str = pydantic.Field(alias='projectId')
    name: str = pydantic.Field(alias='projectName')
    description: Optional[str] = pydantic.Field(default=None, alias='projectDescription')

    slug: Optional[str] = pydantic.Field(default=None, alias='projectSlug')
    full_slug: str = pydantic.Field(default=None, alias='projectFullSlug')

    report_template: Optional[str] = pydantic.Field(default=None, alias='defaultReportTemplateName')
    scope: Optional[str] = pydantic.Field(default=None, alias='projectScope')
    permissions: Optional[Dict] = pydantic.Field(default=None, alias='projectPermissions')
    group: Optional[Group] = pydantic.Field(default=None, alias='group')

    issue_settings: Optional[Dict] = pydantic.Field(default=None, alias='issueSettings')
    is_archived: bool = pydantic.Field(default=None, alias='projectIsArchived')
    archive_date: Optional[str] = pydantic.Field(default=None, alias='projectArchiveDate')

    create_date: Optional[str] = pydantic.Field(default=None, alias='projectCreateDate')
    update_date: Optional[str] = pydantic.Field(default=None, alias='projectUpdateDate')
    start_date: Optional[str] = pydantic.Field(default=None, alias='projectStartDate')
    end_date: Optional[str] = pydantic.Field(default=None, alias='projectEndDate')

    application_connect: Optional[str] = pydantic.Field(default=None, alias='applicationConnect', repr=False)
    connection_id: Optional[str] = pydantic.Field(default=None, alias='projectConnectionId', repr=False)
    connection_name: Optional[str] = pydantic.Field(default=None, alias='connectionName', repr=False)
    last_incoming_pong: Optional[str] = pydantic.Field(default=None, alias='lastIncomingPong', repr=False)
    last_outgoing_ping: Optional[str] = pydantic.Field(default=None, alias='lastOutgoingPing', repr=False)
    connection: Optional[Any] = pydantic.Field(default=None, alias='hive', repr=False, exclude=True)

    @pydantic.field_validator('create_date', 'update_date', 'start_date', 'end_date', mode='before')
    def validate_datetime(cls, value: str) -> str:
        """Validate datetime field."""
        try:
            dt: datetime = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError:
            raise ValueError('Invalid datetime.')
        return datetime.strftime(dt, '%d-%m-%Y %H:%M:%S')

    @pydantic.field_validator('group', mode='before')
    def validate_group(cls, value: Dict) -> Group:
        """Validate group field."""
        return Group(**value)
