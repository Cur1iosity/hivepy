import functools
from typing import Dict, Union

from hivepy.field_management.builder.field_builder import FieldBuilder
from hivepy.schema_management.builders.issue_schema_builder import IssueSchemaBuilder
from hivepy.schema_management.builders.project_schema_builder import ProjectSchemaBuilder
from hivepy.schema_management.models import IssueSchema, ProjectSchema


class SchemaBuilder:
    """Class that builds schema objects."""
    field_builder: FieldBuilder = FieldBuilder()
    issue_schema_builder: IssueSchemaBuilder = IssueSchemaBuilder(field_builder)
    project_schema_builder: ProjectSchemaBuilder = ProjectSchemaBuilder(field_builder)

    @classmethod
    def build(cls, schema_type: str, schema: Dict) -> Union[IssueSchema, ProjectSchema]:
        """Build schema object from raw data."""
        if schema_type == 'issue':
            return cls.issue_schema_builder(schema)
        elif schema_type == 'project':
            return cls.project_schema_builder(schema)
        else:
            raise ValueError(f"Schema type {schema_type} not supported.")

    @functools.partialmethod
    def build_issue_schema(self, schema: Dict) -> IssueSchema:
        """Build IssueSchema object from raw data."""
        return self.build('issue', schema)

    @functools.partialmethod
    def build_project_schema(self, schema: Dict) -> ProjectSchema:
        """Build ProjectSchema object from raw data."""
        return self.build('project', schema)

    def __call__(self, schema_type: str, schema: Dict) -> Union[IssueSchema, ProjectSchema]:
        """Build schema object from raw data."""
        return self.build(schema_type, schema)
