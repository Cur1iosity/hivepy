import json
from datetime import datetime
from typing import Dict, Optional, Any, List, Self

import pydantic


class Project(pydantic.BaseModel):
    """Project model."""
    id: str = pydantic.Field(alias='projectId')
    name: str = pydantic.Field(alias='projectName')
    description: Optional[str] = pydantic.Field(default=None, alias='projectDescription')

    scope: Optional[str] = pydantic.Field(default=None, alias='projectScope', exclude=True)
    permissions: Optional[Dict] = pydantic.Field(default=None, alias='projectPermissions', exclude=True)

    is_archived: bool = pydantic.Field(default=None, alias='projectIsArchived', exclude=True)
    archive_date: Optional[str] = pydantic.Field(default=None, alias='projectArchiveDate', exclude=True)

    create_date: Optional[str] = pydantic.Field(default=None, alias='projectCreateDate', exclude=True)
    update_date: Optional[str] = pydantic.Field(default=None, alias='projectUpdateDate', exclude=True)
    start_date: Optional[str] = pydantic.Field(default=None, alias='projectStartDate')
    end_date: Optional[str] = pydantic.Field(default=None, alias='projectEndDate')
    issue_settings: Optional[Dict] = pydantic.Field(default=None, alias='issueSettings', exclude=True)

    users: Optional[List[Dict]] = pydantic.Field(default=None, alias='projectUsers', exclude=True)

    application_connect: Optional[str] = pydantic.Field(default=None,
                                                        alias='applicationConnect',
                                                        repr=False, exclude=True)
    connection_id: Optional[str] = pydantic.Field(default=None, alias='projectConnectionId', repr=False, exclude=True)
    connection_name: Optional[str] = pydantic.Field(default=None, alias='connectionName', repr=False, exclude=True)
    last_incoming_pong: Optional[str] = pydantic.Field(default=None, alias='lastIncomingPong', repr=False, exclude=True)
    last_outgoing_ping: Optional[str] = pydantic.Field(default=None, alias='lastOutgoingPing', repr=False, exclude=True)
    connection: Optional[Any] = pydantic.Field(default=None, alias='hive', repr=False, exclude=True, init=False)
    api: Optional[Any] = pydantic.Field(default=None, alias='api', repr=False, exclude=True)

    model_config = pydantic.ConfigDict(
        populate_by_name=True,

    )

    def set_api(self, api: Any) -> Self:
        """Set API."""
        self.api = api
        return self

    @pydantic.field_validator('create_date', 'update_date', 'start_date', 'end_date', mode='before')
    def validate_datetime(cls, value: str) -> str:
        """Validate datetime field."""
        try:
            dt: datetime = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError:
            raise ValueError('Invalid datetime.')
        return datetime.strftime(dt, '%d-%m-%Y %H:%M:%S')

    @pydantic.model_serializer(when_used='json')
    def dump(self) -> Dict:
        """Dump model to dictionary."""
        project_data: Dict = self.dict(by_alias=True, exclude_none=True)
        project_description: str = project_data.pop('projectDescription')
        project_name: str = project_data.pop('projectName')
        start_date: str = project_data.pop('projectStartDate')
        end_date: str = project_data.pop('projectEndDate')

        del project_data['projectId']

        return {'data': json.dumps(project_data),
                'projectDescription': project_description,
                'projectName': project_name,
                'projectStartDate': start_date,
                'projectEndDate': end_date}

    def __str__(self) -> str:
        """Return string representation of object."""
        return f'{self.__class__.__name__}({"".join(f"{key}={value}, " for key, value in self.model_dump().items())})'

    def __setattr__(self, name, value) -> None:
        """Set attribute."""
        super().__setattr__(name, value)

        if self.api and name not in ('id', 'api'):
            # Check if the name is one of the model's fields
            if name in self.__fields__:
                # Prepare data for API update
                data = self.api.update_project(self.id, self.dump())
                self.__dict__.update(self.parse_obj(data).__dict__)
