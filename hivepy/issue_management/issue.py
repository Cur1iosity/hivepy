import uuid
from datetime import datetime
from typing import Dict, List, Optional

import pydantic


class Issue(pydantic.BaseModel):
    id: Optional[uuid.UUID] = pydantic.Field(alias='uuid')
    internal_id: Optional[int] = pydantic.Field(default=None, alias='id')
    name: str
    labels: Optional[List[str]] = pydantic.Field(default=None)

    ips: Optional[List[str]] = pydantic.Field(default=None)
    hostnames: Optional[List[str]] = pydantic.Field(default=None)

    status: str
    sync_status: Optional[str] = pydantic.Field(default=None, alias='syncStatus')

    creator: Dict = pydantic.Field(alias='nodeCreator')

    node_id: Optional[str] = pydantic.Field(default=None, alias='nodeId')
    parent_id: Optional[str] = pydantic.Field(default=None, alias='parentId')

    edit_time: datetime = pydantic.Field(default=None, alias='editTime')
    post_time: datetime = pydantic.Field(default=None, alias='postTime')

    checkmarks: Optional[List] = pydantic.Field(default=None)
    assets: Optional[List] = pydantic.Field(default=None)

    issue_source_type: Optional[str] = pydantic.Field(default=None, alias='issueSourceType')
    weakness_type: Optional[str] = pydantic.Field(default=None, alias='weaknessType')

    cvss_vector: Optional[str] = pydantic.Field(default=None, alias='cvssVector')
    cvss_score: Optional[float] = pydantic.Field(default=None, alias='cvssScore')

    probability_score: int = pydantic.Field(default=None, alias='probabilityScore')
    criticality_score: int = pydantic.Field(default=None, alias='criticalityScore')

    requests: Optional[List[Dict]] = pydantic.Field(default=None)
    notes: Optional[List] = pydantic.Field(default=None)
    files: Optional[List[Dict]] = pydantic.Field(default=None)

    general_description: Optional[str] = pydantic.Field(default=None, alias='generalDescription')
    recommendations: Optional[str] = pydantic.Field(default=None)
    reproduce_description: Optional[str] = pydantic.Field(default=None, alias='reproduceDescription')
    risk_description: Optional[str] = pydantic.Field(default=None, alias='riskDescription')
    technical_description: Optional[str] = pydantic.Field(default=None, alias='technicalDescription')

    model_config = pydantic.ConfigDict(
        populate_by_name=True
    )

    # @pydantic.field_validator('post_time', 'edit_time', mode='before')
    # def validate_datetime(cls, value: str) -> str:
    #     """Validate datetime field."""
    #     try:
    #         dt: datetime = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
    #     except ValueError:
    #         raise ValueError('Invalid datetime.')
    #     return datetime.strftime(dt, '%d-%m-%Y %H:%M:%S')

    @pydantic.model_validator(mode='before')
    def make_additional_fields_flat(cls, value: Dict) -> Dict:
        """Make additional fields flat."""
        if not (additional_fields := value.get('additionalFields', {})):
            return value
        value.update(additional_fields)
        return value

    def __str__(self) -> str:
        """Return string representation of object."""
        return f'{self.__class__.__name__}({"".join(f"{key}={value}, " for key, value in self.model_dump().items())})'
