import uuid
from datetime import datetime
from typing import Dict, List, Optional, Any, Self

import pydantic


class Issue(pydantic.BaseModel):
    """Issue model."""
    id: Optional[uuid.UUID] = pydantic.Field(alias='uuid')
    project_id: Optional[str] = pydantic.Field(default=None, alias='projectId')
    internal_id: Optional[int] = pydantic.Field(default=None, alias='id', exclude=True)
    name: str
    labels: Optional[List[str]] = pydantic.Field(default=None, exclude=True)

    ips: Optional[List[str]] = pydantic.Field(default=None)
    hostnames: Optional[List[str]] = pydantic.Field(default=None)
    assets: Optional[List[Dict]] = pydantic.Field(default=None)

    status: str
    sync_status: Optional[str] = pydantic.Field(default=None, alias='syncStatus', exclude=True)

    creator: Dict = pydantic.Field(alias='nodeCreator', exclude=True)

    node_id: Optional[str] = pydantic.Field(default=None, alias='nodeId', exclude=True)
    parent_id: Optional[str] = pydantic.Field(default=None, alias='parentId', exclude=True)

    edit_time: datetime = pydantic.Field(default=None, alias='editTime', exclude=True)
    post_time: datetime = pydantic.Field(default=None, alias='postTime', exclude=True)

    checkmarks: Optional[List] = pydantic.Field(default=None, alias='checkmarks')

    issue_source_type: Optional[str] = pydantic.Field(default=None, alias='issueSourceType')
    weakness_type: Optional[str] = pydantic.Field(default=None, alias='weaknessType')

    cvss_vector: Optional[str] = pydantic.Field(default=None, alias='cvssVector')
    cvss_score: Optional[float] = pydantic.Field(default=None, alias='cvssScore')

    probability_score: int = pydantic.Field(default=None, alias='probabilityScore')
    criticality_score: int = pydantic.Field(default=None, alias='criticalityScore')

    requests: Optional[List[Dict]] = pydantic.Field(default=None, alias='requests')
    notes: Optional[List] = pydantic.Field(default=None, alias='notes')
    files: Optional[List[Dict]] = pydantic.Field(default=None, alias='files')

    general_description: Optional[str] = pydantic.Field(default=None, alias='generalDescription')
    recommendations: Optional[str] = pydantic.Field(default=None)
    reproduce_description: Optional[str] = pydantic.Field(default=None, alias='reproduceDescription')
    risk_description: Optional[str] = pydantic.Field(default=None, alias='riskDescription')
    technical_description: Optional[str] = pydantic.Field(default=None, alias='technicalDescription')

    api: Optional[Any] = pydantic.Field(default=None, alias='api', repr=False, exclude=True)

    model_config = pydantic.ConfigDict(
        populate_by_name=True
    )

    def set_api(self, api: Any) -> Self:
        """Set API."""
        self.api = api
        return self

    @pydantic.model_validator(mode='before')
    def make_additional_fields_flat(cls, value: Dict) -> Dict:
        """Make additional fields flat."""
        if not (additional_fields := value.get('additionalFields', {})):
            return value
        value.update(additional_fields)
        return value

    @pydantic.model_serializer(when_used='json')
    def dump(self) -> Dict:
        """Dump model to dictionary."""
        issue_data: Dict = self.dict(by_alias=True, exclude_none=True)
        additional_fields: Dict = {
            'generalDescription': issue_data.pop('generalDescription'),
            'recommendations': issue_data.pop('recommendations'),
            'reproduceDescription': issue_data.pop('reproduceDescription'),
            'riskDescription': issue_data.pop('riskDescription'),
            'technicalDescription': issue_data.pop('technicalDescription'),
        }
        return issue_data | additional_fields

    def __setattr__(self, name, value) -> None:
        """Set attribute."""
        super().__setattr__(name, value)

        if self.api and name not in ('id', 'api'):
            # Check if the name is one of the model's fields
            if name in self.__fields__:
                # Prepare data for API update
                data = self.api.update_issue(self.project_id, self.id, self.dump())
                self.__dict__.update(self.parse_obj(data).__dict__)

    def __str__(self) -> str:
        """Return string representation of object."""
        return f'{self.__class__.__name__}({"".join(f"{key}={value}, " for key, value in self.model_dump().items())})'
