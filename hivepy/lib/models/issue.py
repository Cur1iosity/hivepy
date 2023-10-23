import datetime
from typing import Optional, List, Dict, Any
from uuid import UUID

import pydantic


class Issue(pydantic.BaseModel):
    uuid: str = pydantic.Field(alias='uuid')
    name: str = pydantic.Field(alias='name')
    hostnames: List[str] = pydantic.Field(alias='hostnames')
    ip_addresses: List[str] = pydantic.Field(alias='ips')
    cvss_vector: Optional[str] = pydantic.Field( default=None, alias='cvssVector')
    cvss_score: Optional[float] = pydantic.Field(default=None, alias='cvssScore')
    weakness_type: Optional[str] = pydantic.Field(default=None, alias='weaknessType')
    checkmark_count: int = pydantic.Field(alias='checkmarkCount')
    issueSource: Optional[str] = pydantic.Field(default=None, alias='issueSourceType')

    probability_score: Optional[float] = pydantic.Field(default=None, alias='probabilityScore')
    criticality_score: Optional[float] = pydantic.Field(default=None, alias='criticalityScore')
    total_score: Optional[float] = pydantic.Field(default=None, alias='totalScore')

    labels: Optional[List[str]] = pydantic.Field(default=None, alias='labels')
    post_time: Optional[str] = pydantic.Field(default=None, alias='postTime')

    additional_fields: Optional[Dict] = pydantic.Field(default=None, alias='additionalFields')

    note_count: Optional[int] = pydantic.Field(default=None, alias='noteCount')
    notes: Optional[List] = pydantic.Field(default=None, alias='notes')

    files: Optional[List[Dict]] = pydantic.Field(default=None, alias='files')
    requests: Optional[List[Dict]] = pydantic.Field(default=None, alias='requests')

    status: str = pydantic.Field(alias='status')

    internal_id: int = pydantic.Field(alias='id')
    sync_status: Optional[str] = pydantic.Field(default=None, alias='syncStatus')
    node_id: Optional[str] = pydantic.Field(default=None, alias='nodeId')
    parent_id: Optional[str] = pydantic.Field(default=None, alias='parentId')
    message_count_brig: Optional[int] = pydantic.Field(default=0, alias='messageCountBrig')
    message_count_frigate: Optional[int] = pydantic.Field(default=0, alias='messageCountFrigate')

    creator_uuid: str = pydantic.Field(alias='creatorUuid')
    connection: Optional[Any] = pydantic.Field(default=None, alias='hive', repr=False, exclude=True)

    @pydantic.field_validator('post_time', mode='before')
    def validate_datetime(cls, value: str) -> str:
        """Validate datetime field."""
        try:
            dt: datetime.datetime = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError:
            raise ValueError('Invalid datetime.')
        return datetime.datetime.strftime(dt, '%d-%m-%Y %H:%M:%S')

    @pydantic.field_validator('uuid', 'creator_uuid', mode='before')
    def validate_id(cls, value: str) -> str:
        """Validate hive id-type field."""
        try:
            UUID(value)
        except ValueError:
            raise ValueError('Invalid vulnerability id.')
        return value

    @pydantic.model_serializer
    def serialize(self) -> Dict:
        """Serialize object to dict."""
        additional_fields = (dump := self.model_dump()).pop('additional_fields') or {}
        return dump | additional_fields

    pydantic.ConfigDict(
        populate_by_name=True,
    )

    def __str__(self) -> str:
        """Return string representation of object."""
        return f'{self.__class__.__name__}({"".join(f"{key}={value}, " for key, value in self.model_dump().items())})'
