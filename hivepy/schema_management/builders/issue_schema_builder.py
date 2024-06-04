from typing import Optional

from hivepy.field_management.builder.field_builder import FieldBuilder
from hivepy.schema_management.models.issue_schema import IssueSchema


class IssueSchemaBuilder:
    """Class that builds an IssueSchema object from a raw issue schema dictionary."""
    def __init__(self, field_builder=None):
        self.field_builder: Optional[FieldBuilder] = field_builder

    def build(self, issue_schema: dict) -> IssueSchema:
        """Build ProjectSchema object from raw data."""
        data = issue_schema.copy()
        raw_additional_fields = data.pop('additionalFieldsSettings', [])
        raw_predefined_fields = data.pop('predefinedFieldsSettings', [])
        data['additionalFieldsSettings'] = [self.field_builder.build(field) for field in raw_additional_fields]
        data['predefinedFieldsSettings'] = [self.field_builder.build(field) for field in raw_predefined_fields]
        return IssueSchema(**data)

    def __call__(self, project_schema: dict) -> IssueSchema:
        """Build ProjectSchema object from raw data."""
        return self.build(project_schema)
