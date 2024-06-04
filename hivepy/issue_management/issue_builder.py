from typing import Dict, Type, Optional, Any

import pydantic

from hivepy.issue_management.issue import Issue
from hivepy.schema_management.factories.schema_factory import SchemaFactory
from hivepy.schema_management.models.issue_schema import IssueSchema


class IssueBuilder:
    def __init__(self, schema_factory=None) -> None:
        """Initialize the project builder with a template builder."""
        self.schema_factory: SchemaFactory = schema_factory if schema_factory \
            else self.create_schema_factory()

    @staticmethod
    def create_schema_factory() -> SchemaFactory:
        """Create a project schema builder."""
        return SchemaFactory()

    def build(self, issue_schema: IssueSchema,  issue_data: Dict) -> Issue:
        """Build a project from the given project data."""
        issue_model = self.create_issue_model(issue_schema)
        return issue_model(**issue_data)

    @staticmethod
    def create_issue_model(schema: IssueSchema) -> Type['Issue']:
        """Create a project model from the given project schema."""
        fields = schema.predefined_fields_settings + schema.additional_fields_settings
        schema_fields = {field.name: (Optional[Any], None) for field in fields}
        return pydantic.create_model('Issue', **schema_fields, __base__=Issue)
